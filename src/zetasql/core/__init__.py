"""ZetaSQL Core Layer - WASI Communication & ProtoModel Infrastructure.

This package provides the foundational Layer 1 infrastructure:

API layer depend on this core infrastructure.
"""

from .exceptions import (
    ClientError,
    IllegalStateError,
    InvalidArgumentError,
    ServerError,
    StatusCode,
    ZetaSQLError,
)
from .local_service import ZetaSqlLocalService
from .wasm_client import WasmClient

__all__ = [
    "ClientError",
    "IllegalStateError",
    "InvalidArgumentError",
    "ServerError",
    "StatusCode",
    "WasmClient",
    "ZetaSQLError",
    "ZetaSqlLocalService",
]
