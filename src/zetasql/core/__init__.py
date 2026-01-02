"""ZetaSQL Core Layer - WASI Communication & ProtoModel Infrastructure.

This package provides the foundational Layer 1 infrastructure:

- wasm_client: Low-level WASM runtime and memory management
- local_service: Direct wrapper around ZetaSQL LocalService gRPC methods
- exceptions: Error handling and status codes
- func_utils: Parameter decorator utilities

All higher layers (api, extensions) depend on this core infrastructure.
"""

__all__ = [
    'WasmClient',
    'ZetaSqlLocalService',
    'StatusCode',
    'ZetaSQLError',
    'ServerError',
    'ClientError',
    'InvalidArgumentError',
    'IllegalStateError',
]

from zetasql.core.wasm_client import WasmClient
from zetasql.core.local_service import ZetaSqlLocalService
from zetasql.core.exceptions import (
    StatusCode,
    ZetaSQLError,
    ServerError,
    ClientError,
    InvalidArgumentError,
    IllegalStateError,
)
