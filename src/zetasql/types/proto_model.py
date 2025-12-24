"""
ZetaSQL Proto Model Base

Base classes and utilities for working with ZetaSQL proto models.
"""

from google.protobuf import message as _message
from typing import TypeVar, cast

T = TypeVar("T", bound="ProtoModel")

class ProtoModel:
    """Base class for all ZetaSQL wrapper classes"""
    
    @classmethod
    def from_proto(cls: type[T], proto: _message.Message) -> T:
        """
        Create a proto model instance from a proto object (simple constructor).
        
        This is a minimal constructor that directly wraps the proto without
        any type resolution. For union types, use parse_proto() instead.
        
        Args:
            proto: A proto message instance
            
        Returns:
            Proto model instance of the calling class type
            
        Example:
            >>> proto = resolved_ast_pb2.ResolvedFilterScanProto()
            >>> scan = ResolvedFilterScan.from_proto(proto)
            >>> # scan is ResolvedFilterScan instance
        """
        # Create instance without calling __init__
        instance = object.__new__(cls)
        instance._proto = proto
        return instance
    
    def as_type(self, model_type: type[T]) -> T:
        """
        Cast proto model to a specific type with runtime validation.
        
        This is useful for type narrowing in IDEs after isinstance checks.
        
        Args:
            model_type: The proto model class to cast to
            
        Returns:
            Self cast to the specified type
            
        Raises:
            TypeError: If the proto model is not an instance of model_type
            
        Example:
            >>> scan = some_union_scan
            >>> if isinstance(scan, ResolvedFilterScan):
            ...     filter_scan = scan.as_type(ResolvedFilterScan)
            ...     print(filter_scan.filter_expr)  # IDE autocomplete works
        """
        if not isinstance(self, model_type):
            raise TypeError(
                f"Cannot cast {type(self).__name__} to {model_type.__name__}. "
                f"Instance is not of the target type."
            )
        return cast(T, self)


def parse_proto(proto: _message.Message) -> ProtoModel:
    """
    Parse a proto object to its concrete proto model type.
    
    This is the recommended way to create proto models from protos.
    For union types (oneof), it automatically resolves to the concrete type.
    For regular protos, it wraps them in the appropriate proto model class.
    
    This function is idempotent: calling it on a proto multiple times will
    return equivalent proto model instances (same type, same proto).
    
    Args:
        proto: A proto message that may be a union type
        
    Returns:
        A proto model instance of the concrete type
        
    Example:
        >>> # Regular proto
        >>> proto = resolved_ast_pb2.ResolvedFilterScanProto()
        >>> scan = parse_proto(proto)
        >>> type(scan).__name__
        'ResolvedFilterScan'
        
        >>> # Union type proto - automatically resolves to concrete
        >>> any_scan_proto = resolved_ast_pb2.AnyResolvedScanProto()
        >>> any_scan_proto.resolved_filter_scan_node.CopyFrom(filter_proto)
        >>> model = parse_proto(any_scan_proto)
        >>> type(model).__name__  # Resolved to concrete type
        'ResolvedFilterScan'
    """
    try:
        # Check which variant is set
        which = proto.WhichOneof('node')
        if not which:
            # No variant set, create Any* model as fallback
            return _create_model_from_proto(proto)
    except ValueError:
        # WhichOneof raised an error or 'node' doesn't exist
        # This is not a oneof type
        return _create_model_from_proto(proto)
    
    # Get the proto of the active variant
    try:
        variant_proto = getattr(proto, which)
    except AttributeError:
        # Shouldn't happen, but be defensive
        return _create_model_from_proto(proto)
    
    # Recursively parse the variant (in case it's also a oneof)
    return parse_proto(variant_proto)


def _create_model_from_proto(proto: _message.Message) -> ProtoModel:
    """
    Create proto model instance from a proto by looking up the model class.
    
    Maps proto class name to model class name by removing 'Proto' suffix.
    For nested messages, uses the full proto path to construct the model name.
    Uses object.__new__() to create instances without calling __init__.
    """
    # Import the module at runtime to avoid circular imports
    import zetasql.types.proto_models as model_module

    proto_type_name = type(proto).__name__.removesuffix('Proto')
    
    # Try to get full name from DESCRIPTOR for nested messages
    model_class_name = None
    if hasattr(proto, 'DESCRIPTOR') and hasattr(proto.DESCRIPTOR, 'full_name'):
        full_name = cast(str, proto.DESCRIPTOR.full_name)
        # full_name is like: zetasql.AllowedHintsAndOptionsProto.HintProto
        # We need to convert this to: AllowedHintsAndOptionsHint
        
        # For nested messages, we need parent + child names
        # e.g., "zetasql.AllowedHintsAndOptionsProto.HintProto" -> "AllowedHintsAndOptionsHint"
        # But for top-level messages, we just need the last part
        # e.g., "zetasql.local_service.ParseResponse" -> "ParseResponse"
        
        parts = full_name.split('.')
        # Find message parts (skip package names)
        # If we have something like A.B.C, where A is package:
        # - If B ends with Proto and C exists: B + C is nested (AllowedHintsAndOptionsProto.HintProto)
        # - Otherwise: C is top-level (local_service.ParseResponse)
        
        if len(parts) >= 2:
            # Check if second-to-last part ends with Proto (indicates parent message)
            if len(parts) >= 3:
                # Nested message: combine parent + child
                # e.g., AllowedHintsAndOptionsProto.HintProto -> AllowedHintsAndOptionsHint
                sub_names = [part.removesuffix('Proto') for part in parts[-2:]]
                model_class_name = ''.join(sub_names)
            else:
                # Top-level message: use last part only
                # e.g., local_service.ParseResponse -> ParseResponse
                last_part = parts[-1]
                model_class_name = last_part.removesuffix('Proto')
    
    model_class = getattr(model_module, model_class_name, ProtoModel)
    if not issubclass(model_class, ProtoModel):
        model_class = ProtoModel
    return model_class.from_proto(proto)
