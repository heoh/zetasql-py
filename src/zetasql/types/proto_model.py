"""
ZetaSQL Proto Model Base

Base classes and utilities for working with ZetaSQL proto models.
"""

from google.protobuf import message as _message
from typing import TypeVar, cast, ClassVar, Dict, Any, TYPE_CHECKING
from dataclasses import fields as dataclass_fields, MISSING
from enum import IntEnum

T = TypeVar("T", bound="ProtoModel")


def _convert_to_enum(value: int, field_meta: Dict[str, Any], model_cls: type) -> Any:
    """
    Convert an integer enum value to its IntEnum representation.
    
    Args:
        value: The integer value from proto
        field_meta: Field metadata containing enum type information
        model_cls: The model class that contains this field
        
    Returns:
        IntEnum instance if conversion is possible, otherwise the original int value
    """
    if value == 0:
        # Proto default value - might not be set, so just return as-is
        # IntEnum will handle it if needed
        pass
    
    enum_type_name = field_meta.get('enum_type_name')
    enum_parent_msg = field_meta.get('enum_parent_message')
    
    if not enum_type_name:
        return value
    
    # Try to find the enum class
    enum_cls = None
    
    # First check if it's a nested enum in the model class
    if enum_parent_msg:
        # Look for ParentClass.EnumType
        # Need to search in the module where model_cls is defined
        import sys
        module = sys.modules.get(model_cls.__module__)
        if module:
            parent_cls = getattr(module, enum_parent_msg, None)
            if parent_cls:
                enum_cls = getattr(parent_cls, enum_type_name, None)
    
    # If not found as nested, try as top-level in the same module
    if not enum_cls:
        import sys
        module = sys.modules.get(model_cls.__module__)
        if module:
            enum_cls = getattr(module, enum_type_name, None)
    
    # Convert to IntEnum if class was found
    if enum_cls and isinstance(enum_cls, type) and issubclass(enum_cls, IntEnum):
        try:
            return enum_cls(value)
        except ValueError:
            # Value not in enum, return as int
            return value
    
    return value


class ProtoModel:
    """Base class for all ZetaSQL wrapper classes (dataclass-based concrete models)"""
    
    # Subclasses should define these as ClassVar
    _PROTO_CLASS: ClassVar[type] = None
    _PROTO_FIELD_MAP: ClassVar[Dict[str, Dict[str, Any]]] = {}
    
    @classmethod
    def from_proto(cls: type[T], proto: _message.Message) -> T:
        """
        Create a proto model instance from a proto object using MRO-based parent chain tracking.
        
        This dynamically traverses the class hierarchy (MRO) to determine parent depth
        and extracts fields from the appropriate proto.parent levels.
        
        Args:
            proto: A proto message instance
            
        Returns:
            Proto model instance with all fields populated from proto
            
        Example:
            >>> proto = resolved_ast_pb2.ResolvedLiteralProto()
            >>> proto.value.CopyFrom(...)
            >>> proto.parent.type.type_kind = 2
            >>> literal = ResolvedLiteral.from_proto(proto)
            >>> # literal.value and literal.type are populated
        """
        kwargs = {}
        
        # Get all ProtoModel classes in MRO (excluding ProtoModel itself)
        proto_model_classes = [
            c for c in cls.__mro__
            if c != ProtoModel and issubclass(c, ProtoModel) and hasattr(c, '_PROTO_FIELD_MAP')
        ]
        
        # Reverse to process from ancestor to descendant
        proto_model_classes.reverse()
        
        # Calculate max depth (number of parent levels)
        max_depth = len(proto_model_classes) - 1
        
        # Process each class level
        for i, ancestor_cls in enumerate(proto_model_classes):
            # Calculate parent depth for this class
            # Most distant ancestor has highest depth
            depth = max_depth - i
            
            # Navigate to the appropriate parent level
            current_proto = proto
            for _ in range(depth):
                if not hasattr(current_proto, 'parent'):
                    # Proto doesn't have parent field, skip this ancestor
                    break
                current_proto = current_proto.parent
            
            # Detect oneof fields to only extract the active variant
            # Build a set of field names that belong to oneofs
            oneof_fields = {}  # Maps field_name -> oneof_name
            if hasattr(current_proto, 'DESCRIPTOR') and hasattr(current_proto.DESCRIPTOR, 'oneofs'):
                for oneof_desc in current_proto.DESCRIPTOR.oneofs:
                    oneof_name = oneof_desc.name
                    for field_desc in oneof_desc.fields:
                        oneof_fields[field_desc.name] = oneof_name
            
            # Build a set of active oneof fields
            active_oneof_fields = set()
            for oneof_name in set(oneof_fields.values()):
                try:
                    which_field = current_proto.WhichOneof(oneof_name)
                    if which_field:
                        active_oneof_fields.add(which_field)
                except (ValueError, AttributeError):
                    pass
            
            # Extract fields defined by this ancestor class
            field_map = ancestor_cls._PROTO_FIELD_MAP
            for field_name, field_meta in field_map.items():
                proto_field = field_meta['proto_field']
                
                if not hasattr(current_proto, proto_field):
                    continue
                
                # Skip oneof fields that are not active
                if proto_field in oneof_fields and proto_field not in active_oneof_fields:
                    continue
                
                value_obj = getattr(current_proto, proto_field)
                
                # Convert proto value to model value
                if field_meta['is_message']:
                    if field_meta.get('is_repeated', False):
                        kwargs[field_name] = [parse_proto(item) for item in value_obj]
                    else:
                        # Check if message has content
                        kwargs[field_name] = parse_proto(value_obj) if value_obj.ByteSize() > 0 else None
                elif field_meta.get('is_enum', False):
                    # Enum type - convert int to IntEnum if possible
                    if field_meta.get('is_repeated', False):
                        # Repeated enum field
                        enum_values = []
                        for enum_val in value_obj:
                            converted = _convert_to_enum(enum_val, field_meta, cls)
                            if converted is not None:
                                enum_values.append(converted)
                        kwargs[field_name] = enum_values
                    else:
                        # Singular enum field
                        kwargs[field_name] = _convert_to_enum(value_obj, field_meta, cls)
                else:
                    # Primitive type
                    kwargs[field_name] = value_obj
        
        return cls(**kwargs)
    
    def to_proto(self) -> _message.Message:
        """
        Export proto model to protobuf message using MRO-based parent chain reconstruction.
        
        This dynamically constructs the proto message by placing fields at the appropriate
        proto.parent levels based on the class hierarchy.
        
        Returns:
            Protobuf message with all fields populated
            
        Example:
            >>> literal = ResolvedLiteral(value=..., type=...)
            >>> proto = literal.to_proto()
            >>> # proto.value and proto.parent.type are populated
        """
        if self._PROTO_CLASS is None:
            raise NotImplementedError(f"{type(self).__name__} does not define _PROTO_CLASS")
        
        proto = self._PROTO_CLASS()
        
        # Get all ProtoModel classes in MRO
        proto_model_classes = [
            c for c in type(self).__mro__
            if c != ProtoModel and issubclass(c, ProtoModel) and hasattr(c, '_PROTO_FIELD_MAP')
        ]
        proto_model_classes.reverse()
        max_depth = len(proto_model_classes) - 1
        
        # Process each class level
        for i, ancestor_cls in enumerate(proto_model_classes):
            depth = max_depth - i
            
            # Navigate to target proto level
            current_proto = proto
            for _ in range(depth):
                current_proto = getattr(current_proto, 'parent', current_proto)
            
            # Set fields defined by this ancestor
            field_map = ancestor_cls._PROTO_FIELD_MAP
            
            for field_name, field_meta in field_map.items():
                value = getattr(self, field_name, None)
                
                # Skip None values (not explicitly set by user)
                if value is None:
                    continue
                
                proto_field = field_meta['proto_field']
                
                if not hasattr(current_proto, proto_field):
                    continue
                
                if field_meta['is_message']:
                    if field_meta.get('is_repeated', False):
                        # Check if it's a map field (dict in Python)
                        if isinstance(value, dict):
                            # Map field: Dict[K, V] -> protobuf map
                            target_map = getattr(current_proto, proto_field)
                            target_map.clear()
                            for key, val in value.items():
                                if isinstance(val, ProtoModel):
                                    target_map[key].CopyFrom(val.to_proto())
                                else:
                                    target_map[key].CopyFrom(val)
                        else:
                            # Regular repeated message field
                            # Skip if value is empty list (default)
                            if not value:
                                continue
                            target_list = getattr(current_proto, proto_field)
                            target_list.clear()
                            for item in value:
                                if isinstance(item, ProtoModel):
                                    target_list.add().CopyFrom(item.to_proto())
                                else:
                                    target_list.append(item)
                    else:
                        # Singular message field
                        if isinstance(value, ProtoModel):
                            getattr(current_proto, proto_field).CopyFrom(value.to_proto())
                        else:
                            getattr(current_proto, proto_field).CopyFrom(value)
                else:
                    # Primitive field
                    if field_meta.get('is_repeated', False):
                        # Repeated primitive field (e.g., List[int])
                        # Skip if value is empty list (default)
                        if not value:
                            continue
                        target_list = getattr(current_proto, proto_field)
                        del target_list[:]  # Clear existing
                        for item in value:
                            target_list.append(item)
                    else:
                        # Singular primitive field
                        # Value is not None, so user explicitly set it - always set in proto
                        setattr(current_proto, proto_field, value)
        
        return proto
    
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


def _is_pascal_case(name: str) -> bool:
    """Check if a name is in PascalCase (starts with uppercase)."""
    return len(name) > 0 and name[0].isupper()


def _create_model_from_proto(proto: _message.Message) -> ProtoModel:
    """
    Create proto model instance from a proto by looking up the model class.
    
    Maps proto class name to model class name by removing 'Proto' suffix.
    For nested messages, uses the full proto path to construct the model name.
    Uses from_proto() classmethod to create instances (dataclass-based).
    """
    # Import the module at runtime to avoid circular imports
    import zetasql.types.proto_models as model_module

    proto_type_name = type(proto).__name__.removesuffix('Proto')
    
    # Try to get full name from DESCRIPTOR for nested messages
    model_class_name = None
    if hasattr(proto, 'DESCRIPTOR') and hasattr(proto.DESCRIPTOR, 'full_name'):
        full_name = cast(str, proto.DESCRIPTOR.full_name)
        # full_name examples:
        # - "zetasql.local_service.ParseResponse" (top-level)
        # - "zetasql.local_service.ExtractTableNamesFromNextStatementResponse.TableName" (nested)
        # - "zetasql.AllowedHintsAndOptionsProto.HintProto" (nested with Proto suffix)
        
        parts = full_name.split('.')
        
        # Find class name parts by looking for PascalCase names
        # Package/module names are lowercase or snake_case, class names are PascalCase
        pascal_parts = [part for part in parts if _is_pascal_case(part)]
        
        if pascal_parts:
            # Remove Proto suffix from each part
            class_parts = [part.removesuffix('Proto') for part in pascal_parts]
            
            # For nested classes, navigate through parent classes
            # Example: ["AllowedHintsAndOptions", "Hint"] -> AllowedHintsAndOptions.Hint
            if len(class_parts) > 1:
                # Navigate through nested structure
                current_class = getattr(model_module, class_parts[0], None)
                if current_class:
                    for nested_part in class_parts[1:]:
                        current_class = getattr(current_class, nested_part, None)
                        if not current_class:
                            break
                    if current_class and issubclass(current_class, ProtoModel):
                        return current_class.from_proto(proto)
            
            # Fallback: try flat name (old style for compatibility)
            # ["AllowedHintsAndOptions", "Hint"] -> "AllowedHintsAndOptionsHint"
            model_class_name = ''.join(class_parts)
    else:
        # No DESCRIPTOR, use proto type name
        model_class_name = proto_type_name
    
    model_class = getattr(model_module, model_class_name, ProtoModel)
    if not issubclass(model_class, ProtoModel):
        model_class = ProtoModel
    return model_class.from_proto(proto)
