"""
ZetaSQL Wrapper Utilities

Utility functions for working with ZetaSQL wrapper classes.
"""

from typing import TypeVar, Any
from zetasql.resolved_ast_wrapper import WrapperBase


T = TypeVar('T', bound=WrapperBase)


def node_kind(wrapper: WrapperBase) -> str:
    """
    Get the concrete type name of a wrapper instance.
    
    Args:
        wrapper: A wrapper instance
        
    Returns:
        The class name of the wrapper (e.g., 'ResolvedFilterScan')
        
    Example:
        >>> scan = ResolvedFilterScan(proto)
        >>> node_kind(scan)
        'ResolvedFilterScan'
    """
    return type(wrapper).__name__


def resolve_type(wrapper: T) -> T:
    """
    Resolve a wrapper to its concrete type.
    
    For wrapper instances that represent oneof unions (detected by the presence
    of WhichOneof('node') on their proto), this returns a wrapper instance of
    the concrete variant type. For already-concrete types, returns the input
    unchanged.
    
    This function is idempotent: calling it multiple times on the same instance
    or on an already-resolved instance will return the same result.
    
    Args:
        wrapper: A wrapper instance that may be a union type
        
    Returns:
        A wrapper instance of the concrete type, or the original wrapper if
        already concrete or if resolution fails
        
    Example:
        >>> # scan might be AnyResolvedScan (union type)
        >>> scan = resolve_type(scan)
        >>> # Now scan is the concrete type, e.g., ResolvedFilterScan
        >>> isinstance(scan, ResolvedFilterScan)
        True
        
        >>> # Calling on already-concrete type returns same instance
        >>> filter_scan = ResolvedFilterScan(proto)
        >>> resolve_type(filter_scan) is filter_scan
        True
    """
    # Check if this wrapper has a oneof field
    proto = wrapper._proto
    
    # Try to detect oneof by checking for WhichOneof method
    if not hasattr(proto, 'WhichOneof'):
        # Not a oneof type, return as-is
        return wrapper
    
    try:
        # Check which variant is set
        which = proto.WhichOneof('node')
        if not which:
            # No variant set, return as-is
            return wrapper
    except (ValueError, TypeError):
        # WhichOneof raised an error or 'node' doesn't exist
        # This is not a oneof type, return as-is
        return wrapper
    
    # Get the proto of the active variant
    try:
        variant_proto = getattr(proto, which)
    except AttributeError:
        # Shouldn't happen, but be defensive
        return wrapper
    
    # Map the field name to wrapper class name
    # Field names follow pattern: resolved_xxx_scan_node -> ResolvedXxxScan
    # We need to convert snake_case field name to PascalCase class name
    wrapper_class_name = _field_name_to_class_name(which)
    
    # Dynamically get the wrapper class
    try:
        # Import the module at runtime to avoid circular imports
        import zetasql.resolved_ast_wrapper as wrapper_module
        wrapper_class = getattr(wrapper_module, wrapper_class_name, None)
        
        if wrapper_class is None:
            # Class not found, return original
            return wrapper
        
        # Create and return the concrete wrapper instance
        return wrapper_class(variant_proto)
    except Exception:
        # Any error in resolution, return original
        return wrapper


def _field_name_to_class_name(field_name: str) -> str:
    """
    Convert a proto oneof field name to its corresponding wrapper class name.
    
    Examples:
        resolved_filter_scan_node -> ResolvedFilterScan
        resolved_project_scan_node -> ResolvedProjectScan
        resolved_literal_node -> ResolvedLiteral
    """
    # Remove common suffixes
    name = field_name
    if name.endswith('_node'):
        name = name[:-5]  # Remove '_node'
    if name.endswith('_proto'):
        name = name[:-6]  # Remove '_proto'
    
    # Convert snake_case to PascalCase
    parts = name.split('_')
    class_name = ''.join(word.capitalize() for word in parts)
    
    return class_name
