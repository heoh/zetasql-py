import re
from enum import IntEnum


class StatusCode(IntEnum):
    """absl::StatusCode enum values.

    Matches the C++ absl::StatusCode and gRPC status codes.
    See: https://github.com/abseil/abseil-cpp/blob/master/absl/status/status.h
    """
    OK = 0
    CANCELLED = 1
    UNKNOWN = 2
    INVALID_ARGUMENT = 3
    DEADLINE_EXCEEDED = 4
    NOT_FOUND = 5
    ALREADY_EXISTS = 6
    PERMISSION_DENIED = 7
    RESOURCE_EXHAUSTED = 8
    FAILED_PRECONDITION = 9
    ABORTED = 10
    OUT_OF_RANGE = 11
    UNIMPLEMENTED = 12
    INTERNAL = 13
    UNAVAILABLE = 14
    DATA_LOSS = 15
    UNAUTHENTICATED = 16


class ZetaSQLError(Exception):
    """Base exception for ZetaSQL RPC errors.

    Follows the pattern of gRPC's RpcError and database libraries like psycopg2.
    Inherits directly from Exception (not RuntimeError) as this represents
    a specific domain error (SQL analysis/execution), not a generic runtime error.

    Attributes:
        code: absl::StatusCode as StatusCode enum or int
        message: Error message from ZetaSQL
        raw_error: Original error string from C++ ("Code: X, Message: Y")

    Example:
        try:
            response = client.prepare_query(request)
        except ZetaSQLError as e:
            if e.code == StatusCode.INVALID_ARGUMENT:
                print(f"SQL syntax error: {e.message}")
            elif e.code == StatusCode.NOT_FOUND:
                print(f"Table not found: {e.message}")
    """

    def __init__(self, code: int, message: str, raw_error: str):
        self.code = StatusCode(code) if code in StatusCode._value2member_map_ else code
        self.message = message
        self.raw_error = raw_error
        super().__init__(f"[{self.code.name if isinstance(self.code, StatusCode) else f'Code {code}'}] {message}")

    @classmethod
    def from_error_string(cls, error_str: str):
        """Parse error string from C++ format: 'Code: X, Message: Y'

        Args:
            error_str: Error string in format "Code: X, Message: Y"

        Returns:
            ZetaSQLError instance with parsed code and message
        """
        match = re.match(r'Code: (\d+), Message: (.+)', error_str)
        if match:
            code = int(match.group(1))
            message = match.group(2)
            return cls(code, message, error_str)
        # Fallback for unexpected format
        return cls(StatusCode.UNKNOWN, error_str, error_str)


class AnalyzerError(ZetaSQLError):
    """Error during SQL analysis (semantic errors).
    
    Raised when SQL has semantic issues such as:
    - Table not found
    - Column not found or ambiguous
    - Type mismatch
    - Invalid function arguments
    
    Example:
        try:
            stmt = analyzer.analyze_statement(sql)
        except AnalyzerError as e:
            print(f"Analysis failed: {e.message}")
    """
    pass


class InvalidArgumentError(ZetaSQLError):
    """Invalid argument provided to API.
    
    Raised for client-side validation failures such as:
    - Missing required parameters
    - Mutually exclusive parameters both provided
    - Invalid parameter combinations
    - Empty or malformed input
    
    Example:
        try:
            query = builder.prepare()
        except InvalidArgumentError as e:
            print(f"Invalid parameters: {e.message}")
    """
    pass


class ResourceNotFoundError(ZetaSQLError):
    """Requested resource not found.
    
    Raised when a referenced resource doesn't exist:
    - Table not found in catalog
    - Function not found
    - Type not found
    - Registered catalog ID not found
    
    Example:
        try:
            response = service.analyze(sql, catalog)
        except ResourceNotFoundError as e:
            print(f"Resource missing: {e.message}")
    """
    pass


class IllegalStateError(ZetaSQLError):
    """Operation called in illegal state.
    
    Raised when an operation is attempted in an invalid state:
    - Using PreparedQuery after close()
    - Calling methods on disposed objects
    - Invalid operation sequence
    
    Example:
        query.close()
        try:
            query.execute()  # Error: already closed
        except IllegalStateError as e:
            print(f"Invalid state: {e.message}")
    """
    pass

