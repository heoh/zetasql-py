"""ZetaSQL Core Layer - WASI Communication & ProtoModel Infrastructure.

This package provides the foundational Layer 1 infrastructure:

API layer depend on this core infrastructure.
"""

from .wasm_client import WasmClient
from .local_service import ZetaSqlLocalService
from .exceptions import (
    StatusCode,
    ZetaSQLError,
    ServerError,
    ClientError,
    InvalidArgumentError,
    IllegalStateError,
)

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
