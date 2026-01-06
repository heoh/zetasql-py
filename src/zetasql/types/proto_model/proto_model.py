"""
ZetaSQL Proto Model Base

Base classes and utilities for working with ZetaSQL proto models.
"""

from enum import IntEnum
from typing import Any, ClassVar, TypeVar, cast

from google.protobuf import message as _message

T = TypeVar("T", bound="ProtoModel")


def _wrap_in_union_if_needed(value: "ProtoModel", parent_proto: _message.Message, field_name: str) -> _message.Message:
    """
    Check if target field is a union type by examining proto descriptor,
    and wrap the value in appropriate union wrapper if needed.

    Union types are identified by having oneof fields in their descriptor.
    If the target field is a union, we create the corresponding ProtoModel union
    instance and set the appropriate variant field.

    Args:
        value: ProtoModel instance to convert
        parent_proto: Parent proto message containing the target field
        field_name: Name of the field in parent_proto

    Returns:
        Proto message, either wrapped in union or as-is
    """
    # Get the field descriptor from parent proto
    if not hasattr(parent_proto, "DESCRIPTOR"):
        return value.to_proto()

    field_desc = parent_proto.DESCRIPTOR.fields_by_name.get(field_name)
    if not field_desc or not field_desc.message_type:
        # Not a message field or field not found
        return value.to_proto()

    # Check if the target message type has oneofs (characteristic of union types)
    has_oneofs = hasattr(field_desc.message_type, "oneofs") and len(field_desc.message_type.oneofs) > 0
    if not has_oneofs:
        # Not a union type - regular message field
        return value.to_proto()

    # This is a union type! Get the corresponding ProtoModel union class
    union_proto_type_name = field_desc.message_type.name
    union_model_class_name = union_proto_type_name.removesuffix("Proto")

    # Import the union class
    import zetasql.types.proto_model as model_module

    union_class = getattr(model_module, union_model_class_name, None)

    if union_class is None or not issubclass(union_class, ProtoModel):
        # Union class not found, return value as-is
        return value.to_proto()

    # Find which field in the union should hold this value
    # We need to directly create the union proto and set the appropriate oneof field
    # rather than going through ProtoModel to avoid infinite recursion

    # First convert value to proto (this may recursively call _wrap_in_union_if_needed for nested fields)
    value_proto = value.to_proto()
    value_proto_type_name = type(value_proto).__name__

    # Create the union proto instance
    union_proto_class = union_class._PROTO_CLASS
    union_proto = union_proto_class()

    # Find the matching oneof field in the union proto
    # The field name is typically the proto type name in snake_case
    # We need to check for exact match first, then check base classes

    # First try exact match
    for field_desc in union_proto.DESCRIPTOR.fields:
        if field_desc.message_type and field_desc.message_type.name == value_proto_type_name:
            getattr(union_proto, field_desc.name).CopyFrom(value_proto)
            return union_proto

    # No exact match - try to find a base class match by recursively checking nested unions
    def try_nested_union(current_union_proto, visited_types=None):
        """Recursively try to find a matching field in nested unions."""
        if visited_types is None:
            visited_types = set()

        current_type_name = type(current_union_proto).__name__
        if current_type_name in visited_types:
            return None

        visited_types = visited_types | {current_type_name}

        for field_desc in current_union_proto.DESCRIPTOR.fields:
            if not field_desc.message_type:
                continue

            # Check if this field has oneofs (is a union)
            if not (hasattr(field_desc.message_type, "oneofs") and len(field_desc.message_type.oneofs) > 0):
                continue

            nested_union_proto_type_name = field_desc.message_type.name
            nested_union_model_class_name = nested_union_proto_type_name.removesuffix("Proto")

            import zetasql.types.proto_model as model_module

            nested_union_class = getattr(model_module, nested_union_model_class_name, None)

            if not nested_union_class or not issubclass(nested_union_class, ProtoModel):
                continue

            nested_union_proto_class = nested_union_class._PROTO_CLASS
            nested_union_proto = nested_union_proto_class()

            # Try direct match in this nested union
            for nested_field_desc in nested_union_proto.DESCRIPTOR.fields:
                if nested_field_desc.message_type and nested_field_desc.message_type.name == value_proto_type_name:
                    getattr(nested_union_proto, nested_field_desc.name).CopyFrom(value_proto)
                    return (field_desc.name, nested_union_proto)

            # Try deeper nesting recursively
            deeper_result = try_nested_union(nested_union_proto, visited_types)
            if deeper_result:
                deeper_field_name, deeper_union_proto = deeper_result
                getattr(nested_union_proto, deeper_field_name).CopyFrom(deeper_union_proto)
                return (field_desc.name, nested_union_proto)

        return None

    nested_result = try_nested_union(union_proto)
    if nested_result:
        field_name, nested_proto = nested_result
        getattr(union_proto, field_name).CopyFrom(nested_proto)
        return union_proto

    # No matching field found - return value proto as-is
    return value_proto


def _convert_to_enum(value: int, field_meta: dict[str, Any], model_cls: type) -> Any:
    """
    Convert an integer enum value to its IntEnum representation.

    Args:
        value: The integer value from proto
        field_meta: Field metadata containing enum type information
        model_cls: The model class that contains this field

    Returns:
        IntEnum instance if conversion is possible, otherwise the original int value
    """
    enum_type_name = field_meta.get("enum_type_name")
    enum_parent_msg = field_meta.get("enum_parent_message")

    if not enum_type_name:
        return value

    # Try to find the enum class
    import sys

    module = sys.modules.get(model_cls.__module__)
    if not module:
        return value

    enum_cls = None

    # First check if it's a nested enum in the model class
    if enum_parent_msg:
        parent_cls = getattr(module, enum_parent_msg, None)
        if parent_cls:
            enum_cls = getattr(parent_cls, enum_type_name, None)

    # If not found as nested, try as top-level in the same module
    if not enum_cls:
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
    _PROTO_FIELD_MAP: ClassVar[dict[str, dict[str, Any]]] = {}

    @staticmethod
    def _get_proto_model_classes(cls) -> list[type]:
        """Get all ProtoModel classes in MRO, reversed from ancestor to descendant."""
        classes = [
            c for c in cls.__mro__ if c != ProtoModel and issubclass(c, ProtoModel) and hasattr(c, "_PROTO_FIELD_MAP")
        ]
        classes.reverse()
        return classes

    @staticmethod
    def _get_active_oneof_fields(proto: _message.Message) -> set[str]:
        """Build a set of active oneof field names in a proto message."""
        oneof_fields = {}
        if hasattr(proto, "DESCRIPTOR") and hasattr(proto.DESCRIPTOR, "oneofs"):
            for oneof_desc in proto.DESCRIPTOR.oneofs:
                for field_desc in oneof_desc.fields:
                    oneof_fields[field_desc.name] = oneof_desc.name

        active_fields = set()
        for oneof_name in set(oneof_fields.values()):
            try:
                which_field = proto.WhichOneof(oneof_name)
                if which_field:
                    active_fields.add(which_field)
            except (ValueError, AttributeError):
                pass
        return active_fields

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
        proto_model_classes = cls._get_proto_model_classes(cls)
        max_depth = len(proto_model_classes) - 1

        # Process each class level
        for i, ancestor_cls in enumerate(proto_model_classes):
            depth = max_depth - i

            # Navigate to the appropriate parent level
            current_proto = proto
            for _ in range(depth):
                if not hasattr(current_proto, "parent"):
                    break
                current_proto = current_proto.parent

            # Get active oneof fields
            active_oneof_fields = cls._get_active_oneof_fields(current_proto)

            # Build oneof mapping
            oneof_fields = {}
            if hasattr(current_proto, "DESCRIPTOR") and hasattr(current_proto.DESCRIPTOR, "oneofs"):
                for oneof_desc in current_proto.DESCRIPTOR.oneofs:
                    for field_desc in oneof_desc.fields:
                        oneof_fields[field_desc.name] = oneof_desc.name

            # Extract fields defined by this ancestor class
            field_map = ancestor_cls._PROTO_FIELD_MAP
            for field_name, field_meta in field_map.items():
                proto_field = field_meta["proto_field"]

                if not hasattr(current_proto, proto_field):
                    continue

                # Skip oneof fields that are not active
                if proto_field in oneof_fields and proto_field not in active_oneof_fields:
                    continue

                value_obj = getattr(current_proto, proto_field)

                # Convert proto value to model value
                if field_meta["is_message"]:
                    if field_meta.get("is_repeated", False):
                        kwargs[field_name] = [parse_proto(item) for item in value_obj]
                    else:
                        kwargs[field_name] = parse_proto(value_obj) if value_obj.ByteSize() > 0 else None
                elif field_meta.get("is_enum", False):
                    if field_meta.get("is_repeated", False):
                        kwargs[field_name] = [_convert_to_enum(enum_val, field_meta, cls) for enum_val in value_obj]
                    else:
                        kwargs[field_name] = _convert_to_enum(value_obj, field_meta, cls)
                else:
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
        proto_model_classes = self._get_proto_model_classes(type(self))
        max_depth = len(proto_model_classes) - 1

        # Process each class level
        for i, ancestor_cls in enumerate(proto_model_classes):
            depth = max_depth - i

            # Navigate to target proto level
            current_proto = proto
            for _ in range(depth):
                current_proto = getattr(current_proto, "parent", current_proto)

            # Set fields defined by this ancestor
            field_map = ancestor_cls._PROTO_FIELD_MAP

            for field_name, field_meta in field_map.items():
                value = getattr(self, field_name, None)

                # Skip None values (not explicitly set by user)
                if value is None:
                    continue

                proto_field = field_meta["proto_field"]

                if not hasattr(current_proto, proto_field):
                    continue

                if field_meta["is_message"]:
                    self._set_message_field(current_proto, proto_field, value, field_meta)
                else:
                    self._set_primitive_field(current_proto, proto_field, value, field_meta)

        return proto

    @staticmethod
    def _set_message_field(current_proto, proto_field, value, field_meta):
        """Helper method to set message field in proto."""
        if field_meta.get("is_repeated", False):
            if isinstance(value, dict):
                # Map field: Dict[K, V] -> protobuf map
                target_map = getattr(current_proto, proto_field)
                target_map.clear()
                for key, val in value.items():
                    if isinstance(val, ProtoModel):
                        target_map[key].CopyFrom(val.to_proto())
                    else:
                        target_map[key].CopyFrom(val)
            elif value:  # Skip empty lists
                # Regular repeated message field
                target_list = getattr(current_proto, proto_field)
                target_list.clear()
                for item in value:
                    if isinstance(item, ProtoModel):
                        item_proto = _wrap_in_union_if_needed(item, current_proto, proto_field)
                        target_list.add().CopyFrom(item_proto)
                    else:
                        target_list.append(item)
        else:
            # Singular message field
            if isinstance(value, ProtoModel):
                value_proto = _wrap_in_union_if_needed(value, current_proto, proto_field)
                getattr(current_proto, proto_field).CopyFrom(value_proto)
            else:
                getattr(current_proto, proto_field).CopyFrom(value)

    @staticmethod
    def _set_primitive_field(current_proto, proto_field, value, field_meta):
        """Helper method to set primitive field in proto."""
        if field_meta.get("is_repeated", False):
            if value:  # Skip empty lists
                target_list = getattr(current_proto, proto_field)
                del target_list[:]
                target_list.extend(value)
        else:
            setattr(current_proto, proto_field, value)

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
                f"Cannot cast {type(self).__name__} to {model_type.__name__}. Instance is not of the target type."
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
    # Handle non-message types (primitives, enums, strings)
    # This can happen when parse_proto is called on items from repeated fields
    # that contain primitives or enum strings
    if not isinstance(proto, _message.Message):
        return proto

    try:
        # Check which variant is set
        which = proto.WhichOneof("node")
        if not which:
            # No variant set, create Any* model as fallback
            return _create_model_from_proto(proto)
    except ValueError:
        # WhichOneof raised an error or 'node' doesn't exist
        # This is not a oneof type
        return _create_model_from_proto(proto)
    except AttributeError:
        # proto doesn't have WhichOneof method (not a message)
        # This shouldn't happen if the isinstance check works, but be defensive
        return proto

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
    import zetasql.types.proto_model as model_module

    proto_type_name = type(proto).__name__.removesuffix("Proto")

    # Try to get full name from DESCRIPTOR for nested messages
    model_class_name = None
    if hasattr(proto, "DESCRIPTOR") and hasattr(proto.DESCRIPTOR, "full_name"):
        full_name = cast(str, proto.DESCRIPTOR.full_name)
        # full_name examples:
        # - "zetasql.local_service.ParseResponse" (top-level)
        # - "zetasql.local_service.ExtractTableNamesFromNextStatementResponse.TableName" (nested)
        # - "zetasql.AllowedHintsAndOptionsProto.HintProto" (nested with Proto suffix)

        parts = full_name.split(".")

        # Find class name parts by looking for PascalCase names
        # Package/module names are lowercase or snake_case, class names are PascalCase
        pascal_parts = [part for part in parts if _is_pascal_case(part)]

        if pascal_parts:
            # Remove Proto suffix from each part
            class_parts = [part.removesuffix("Proto") for part in pascal_parts]

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
            model_class_name = "".join(class_parts)
    else:
        # No DESCRIPTOR, use proto type name
        model_class_name = proto_type_name

    model_class = getattr(model_module, model_class_name, ProtoModel)
    if not issubclass(model_class, ProtoModel):
        model_class = ProtoModel
    return model_class.from_proto(proto)


__all__ = [
    "ProtoModel",
    "parse_proto",
]
