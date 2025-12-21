from pathlib import Path


def get_wasm_path() -> Path:
    """Get the path to the zetasql.wasm file.
    
    Returns:
        Path: Absolute path to the zetasql.wasm binary file.
        
    Example:
        >>> from zetasql.wasi import get_wasm_path
        >>> wasm_path = get_wasm_path()
        >>> print(wasm_path)
        /path/to/site-packages/zetasql/wasi/zetasql.wasm
    """
    return Path(__file__).parent / "zetasql.wasm"


__all__ = ["get_wasm_path"]
