import contextlib
import os
import sys
from typing import TypeVar

from google.protobuf import empty_pb2, message
from wasmtime import Config, Engine, Linker, Module, Store, WasiConfig

from zetasql.core.exceptions import ServerError

Message = TypeVar("Message", bound=message.Message)

# WASM constants
WASM32_SIZE_T_BYTES = 4
WASM_NULL_PTR = 0


class WasmClient:
    """Client for interacting with ZetaSQL WASM binary."""

    def __init__(self, wasm_path: str):
        """
        Initialize the WASM client.

        Args:
            wasm_path: Path to the .wasm file
        """
        if not os.path.exists(wasm_path):
            raise FileNotFoundError(f"WASM file not found: {wasm_path}")

        # Create WASI config
        wasi = WasiConfig()
        wasi.inherit_stdout()
        wasi.inherit_stderr()
        wasi.inherit_stdin()

        if tzinfo_dir := get_tzinfo_dir():
            wasi.preopen_dir(tzinfo_dir, "/usr/share/zoneinfo")
        else:
            print("[WARNING] tzdata package not installed, timezone features may not work", file=sys.stderr)

        # Create engine with shared memory enabled and WASI context
        config = Config()
        with contextlib.suppress(AttributeError):
            config.shared_memory = True

        engine = Engine(config)
        self.store = Store(engine)
        self.store.set_wasi(wasi)

        self.module = Module.from_file(self.store.engine, wasm_path)

        # Create a linker and add WASI support
        linker = Linker(self.store.engine)
        linker.define_wasi()

        # Instantiate the module with WASI imports
        self.instance = linker.instantiate(self.store, self.module)

        # Cache exports dictionary
        self.exports = self.instance.exports(self.store)

        # Call _initialize if it exists (WASI initialization)
        try:
            init_func = self.exports["_initialize"]
            init_func(self.store)
        except KeyError:
            pass  # _initialize doesn't exist, skip it

        # Get exports
        self.memory = self.exports["memory"]

    def allocate_bytes(self, size: int) -> int:
        """
        Allocate memory in WASM.

        Args:
            size: Number of bytes to allocate

        Returns:
            Pointer to allocated memory
        """
        return self.exports["wasm_malloc"](self.store, size)

    def free_bytes(self, ptr: int) -> None:
        """Free memory in WASM.

        Args:
            ptr: Pointer to memory to free

        Note:
            C++ wasm_free(void* ptr) does not take size parameter.
            The WASM allocator (malloc/free) tracks block sizes internally.
        """
        self.exports["wasm_free"](self.store, ptr)

    def write_bytes(self, ptr: int, data: bytes) -> None:
        """
        Write bytes to WASM memory.

        Args:
            ptr: Pointer to write to
            data: Bytes to write
        """
        mem_data = self.memory.data_ptr()
        for i, byte in enumerate(data):
            mem_data[ptr + i] = byte

    def read_bytes(self, ptr: int, size: int) -> bytes:
        """
        Read bytes from WASM memory.

        Args:
            ptr: Pointer to read from
            size: Number of bytes to read

        Returns:
            Bytes read from memory
        """
        mem_data = self.memory.data_ptr()
        return bytes([mem_data[ptr + i] for i in range(size)])

    def get_last_error(self) -> str:
        """
        Get the last error message from WASM.

        Returns:
            Last error message, or empty string if no error
        """
        error_size = self.exports["wasm_get_last_error_size"](self.store)
        if error_size == 0:
            return ""

        error_ptr = self.exports["wasm_get_last_error"](self.store)
        return self.read_bytes(error_ptr, error_size).decode("utf-8")

    def call_grpc_func(
        self,
        func_name: str,
        request: message.Message,
        response_type: type[Message] = empty_pb2.Empty,
    ) -> Message:
        request_data = request.SerializeToString()
        response_data = self._call_grpc_method(func_name, request_data)
        response = response_type.FromString(response_data)
        return response

    def _call_grpc_method(self, method_name: str, request_data: bytes) -> bytes:
        """
        Call an gRPC method with protobuf serialized request.

        Args:
            method_name: Name of the gRPC method (e.g., "ZetaSqlLocalService_PrepareExpression")
            request_data: Serialized protobuf request

        Returns:
            Serialized protobuf response

        Raises:
            RuntimeError: If the gRPC call fails (returns nullptr)
        """
        if method_name not in self.exports:
            raise ValueError(f"gRPC method not found: {method_name}")

        method = self.exports[method_name]

        # Allocate memory for request
        request_size = len(request_data)
        request_ptr = self.allocate_bytes(request_size)

        # Allocate memory for response_size (output parameter)
        response_size_ptr = self.allocate_bytes(WASM32_SIZE_T_BYTES)

        try:
            # Write request data
            self.write_bytes(request_ptr, request_data)

            # Call the method (returns response_ptr or nullptr on error)
            response_ptr = method(self.store, request_ptr, request_size, response_size_ptr)

            # Check for nullptr (error case)
            if response_ptr == WASM_NULL_PTR:
                error_str = self.get_last_error()
                raise ServerError.from_error_string(error_str)

            # Read response size from output parameter
            response_size_bytes = self.read_bytes(response_size_ptr, WASM32_SIZE_T_BYTES)
            response_size = int.from_bytes(response_size_bytes, byteorder="little")

            # Read response data
            response_data = self.read_bytes(response_ptr, response_size)

            # Free response memory (C++ allocated via malloc, we must free)
            self.free_bytes(response_ptr)

            return response_data

        finally:
            # Always free request memory and response_size_ptr
            self.free_bytes(request_ptr)
            self.free_bytes(response_size_ptr)


def get_tzinfo_dir() -> str | None:
    """Get the directory path for tzdata zoneinfo files.

    Returns:
        str | None: Path to the tzdata zoneinfo directory, or None if not found.
    """
    try:
        import tzdata

        tzdata_dir = os.path.dirname(tzdata.__file__)
        zoneinfo_dir = os.path.join(tzdata_dir, "zoneinfo")
        if os.path.exists(zoneinfo_dir):
            return zoneinfo_dir
    except ImportError:
        pass
    return None
