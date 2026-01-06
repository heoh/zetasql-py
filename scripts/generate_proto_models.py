#!/usr/bin/env python3
"""
ZetaSQL Proto Model Generator

Generates Python proto model classes for ZetaSQL proto messages with:
- Automatic inheritance hierarchy from proto parent fields
- Type hints for IDE autocompletion
- Cross-file dependency resolution

Usage:
    python scripts/generate_proto_models.py
"""

import argparse
import ast
import importlib.util
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from google.protobuf import descriptor

# Constants
PROTO_SUFFIX = "Proto"
MIXIN_SUFFIX = "Mixin"
ZETASQL_PACKAGE = "zetasql"
PROTO_BASE_MODULE = "zetasql.wasi._pb2"

RESERVED_KEYWORDS = frozenset(
    {
        "and",
        "as",
        "assert",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
    }
)

PROTO_TO_PYTHON_TYPES = {
    descriptor.FieldDescriptor.TYPE_STRING: "str",
    descriptor.FieldDescriptor.TYPE_INT64: "int",
    descriptor.FieldDescriptor.TYPE_INT32: "int",
    descriptor.FieldDescriptor.TYPE_UINT64: "int",
    descriptor.FieldDescriptor.TYPE_UINT32: "int",
    descriptor.FieldDescriptor.TYPE_BOOL: "bool",
    descriptor.FieldDescriptor.TYPE_DOUBLE: "float",
    descriptor.FieldDescriptor.TYPE_FLOAT: "float",
    descriptor.FieldDescriptor.TYPE_BYTES: "bytes",
}

CONVERTIBLE_PROTOBUF_TYPES = {
    "Timestamp": ("datetime", "datetime", "ToDatetime"),
    "Duration": ("datetime", "timedelta", "ToTimedelta"),
}


def load_pb2_module(path: Path, base_dir: Path):
    """Dynamically load a _pb2.py module"""
    rel_path = path.relative_to(base_dir)
    module_parts = [*list(rel_path.parts[:-1]), path.stem]
    module_name = f"{PROTO_BASE_MODULE}.{'.'.join(module_parts)}"

    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_message_classes(module) -> list[tuple[str, Any]]:
    """Extract all proto message classes from a module"""
    return [
        (name, obj)
        for name in dir(module)
        if not name.startswith("_")
        and (obj := getattr(module, name))
        and hasattr(obj, "DESCRIPTOR")
        and hasattr(obj.DESCRIPTOR, "fields")
    ]


def get_enum_types(module) -> list[tuple[str, Any]]:
    """Extract all proto enum types from a module"""
    return [
        (name, obj)
        for name in dir(module)
        if not name.startswith("_")
        and (obj := getattr(module, name))
        and hasattr(obj, "DESCRIPTOR")
        and hasattr(obj.DESCRIPTOR, "values")
        and type(obj).__name__ == "EnumTypeWrapper"
    ]


def _remove_suffix(text: str, suffix: str) -> str:
    """Remove suffix from text if present"""
    return text.removesuffix(suffix)


def _extract_field_info(field) -> dict[str, Any]:
    """Extract field information from proto field descriptor"""
    field_info = {
        "name": field.name,
        "type": field.type,
        "is_repeated": field.is_repeated,
        "number": field.number,
    }

    if field.enum_type:
        field_info["enum_type_name"] = field.enum_type.name
        field_info["enum_type_full"] = field.enum_type.full_name

        if "." in field.enum_type.full_name.split(f"{ZETASQL_PACKAGE}.")[-1]:
            parts = field.enum_type.full_name.split(".")
            if len(parts) >= 2:
                field_info["enum_parent_message"] = parts[-2]

    if field.message_type:
        msg_type_name = field.message_type.name
        msg_type_full = field.message_type.full_name

        field_info["message_type"] = msg_type_name
        field_info["message_type_full"] = msg_type_full

        is_map_entry = (
            field.message_type.GetOptions().map_entry
            if hasattr(field.message_type.GetOptions(), "map_entry")
            else False
        )
        field_info["is_map_field"] = is_map_entry

        if is_map_entry:
            key_field = field.message_type.fields_by_name.get("key")
            value_field = field.message_type.fields_by_name.get("value")
            if key_field and value_field:
                field_info["map_key_type"] = key_field.type
                field_info["map_value_type"] = value_field.type
                if value_field.message_type:
                    field_info["map_value_message_type"] = value_field.message_type.name
                    field_info["map_value_message_full"] = value_field.message_type.full_name

        is_external = not msg_type_full.startswith(f"{ZETASQL_PACKAGE}.")
        field_info["is_external"] = is_external

        if is_external and msg_type_full.startswith("google.protobuf."):
            if msg_type_name in CONVERTIBLE_PROTOBUF_TYPES:
                field_info["convert_to_python"] = CONVERTIBLE_PROTOBUF_TYPES[msg_type_name]

            proto_file = field.message_type.file.name
            proto_filename = proto_file.split("/")[-1].replace(".proto", "")
            field_info["external_module"] = f"google.protobuf.{proto_filename}_pb2"
            field_info["external_type"] = msg_type_name

    return field_info


def _resolve_message_model_info(
    msg_type_full: str, msg_type_name: str, all_messages: dict[str, Any]
) -> dict[str, str | None]:
    """Resolve model name and module path for a message type"""
    for _msg_name, msg_info in all_messages.items():
        if msg_info.get("proto_full_path") == msg_type_full:
            return {
                "model_name": _remove_suffix(msg_info["name"], PROTO_SUFFIX),
                "module_path": msg_info["module"],
                "proto_full_path": msg_info.get("proto_full_path", msg_type_name),
            }

    for msg_name, msg_info in all_messages.items():
        if msg_info.get("proto_name") == msg_type_name or msg_name == msg_type_name:
            return {
                "model_name": _remove_suffix(msg_info["name"], PROTO_SUFFIX),
                "module_path": msg_info["module"],
                "proto_full_path": msg_info.get("proto_full_path", msg_type_name),
            }

    return {"model_name": None, "module_path": None, "proto_full_path": None}


def _collect_enum_info(
    enum_type, nested_cls, module_name, parent_class_name: str, parent_proto_class: str
) -> dict[str, Any]:
    """Collect enum information from descriptor"""
    enum_wrapper = getattr(nested_cls, enum_type.name, None)
    if not enum_wrapper:
        return {}

    enum_info = {
        "name": enum_type.name,
        "class": enum_wrapper,
        "module": module_name,
        "file": None,
        "parent_message": parent_class_name,
        "parent_proto_class": parent_proto_class,
        "values": {value.name: value.number for value in enum_type.values},
    }
    return {f"{parent_class_name}.{enum_type.name}": enum_info}


def extract_inheritance_graph(base_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Extract complete inheritance graph and enums from all _pb2.py files"""
    print(f"Scanning {base_dir} for _pb2.py files...")

    all_messages = {}
    all_enums = {}
    module_cache = {}

    def collect_nested_messages(descriptor, parent_cls, parent_name, module_name, parent_proto_path=""):
        """Recursively collect nested message types and enums"""
        nested_messages = {}

        for nested_type in descriptor.nested_types:
            nested_full_model_name = parent_name + _remove_suffix(nested_type.name, PROTO_SUFFIX)
            nested_class_name = _remove_suffix(nested_type.name, PROTO_SUFFIX)
            nested_proto_full_path = nested_type.full_name
            nested_cls = getattr(parent_cls, nested_type.name)

            nested_messages[nested_full_model_name] = {
                "class": nested_cls,
                "module": module_name,
                "name": nested_full_model_name,
                "class_name": nested_class_name,
                "proto_name": nested_type.name,
                "proto_full_path": nested_proto_full_path,
                "parent_model": parent_name,
                "is_nested": True,
            }

            full_proto_class_path = f"{parent_proto_path}.{nested_type.name}" if parent_proto_path else nested_type.name

            for enum_type in nested_type.enum_types:
                enum_info = _collect_enum_info(
                    enum_type, nested_cls, module_name, nested_class_name, full_proto_class_path
                )
                all_enums.update(enum_info)

            sub_nested = collect_nested_messages(
                nested_type, nested_cls, nested_full_model_name, module_name, full_proto_class_path
            )
            nested_messages.update(sub_nested)

        return nested_messages

    for pb2_file in sorted(base_dir.rglob("*_pb2.py")):
        if "__pycache__" in str(pb2_file):
            continue

        print(f"  Loading {pb2_file.relative_to(base_dir)}...")
        try:
            module = load_pb2_module(pb2_file, base_dir)
            module_cache[pb2_file] = module

            for name, cls in get_message_classes(module):
                all_messages[name] = {
                    "class": cls,
                    "module": module.__name__,
                    "name": name,
                    "proto_name": name,
                    "file": pb2_file,
                    "is_nested": False,
                }

                descriptor = cls.DESCRIPTOR
                for enum_type in descriptor.enum_types:
                    parent_class_name = _remove_suffix(name, PROTO_SUFFIX)
                    enum_wrapper = getattr(cls, enum_type.name, None)
                    if enum_wrapper:
                        enum_full_name = f"{parent_class_name}.{enum_type.name}"
                        all_enums[enum_full_name] = {
                            "name": enum_type.name,
                            "class": enum_wrapper,
                            "module": module.__name__,
                            "file": pb2_file,
                            "parent_message": parent_class_name,
                            "parent_proto_class": name,
                            "values": {value.name: value.number for value in enum_type.values},
                        }

                nested = collect_nested_messages(
                    cls.DESCRIPTOR, cls, _remove_suffix(name, PROTO_SUFFIX), module.__name__, name
                )
                all_messages.update(nested)

            for enum_name, enum_cls in get_enum_types(module):
                all_enums[enum_name] = {
                    "name": enum_name,
                    "class": enum_cls,
                    "module": module.__name__,
                    "file": pb2_file,
                    "values": {value.name: value.number for value in enum_cls.DESCRIPTOR.values},
                }

        except Exception as e:
            print(f"  Warning: Failed to load {pb2_file}: {e}")
            continue

    print(f"\nFound {len(all_messages)} proto message classes (including nested)")

    graph = {}

    for _full_name, info in all_messages.items():
        cls = info["class"]
        descriptor = cls.DESCRIPTOR
        is_nested = info.get("is_nested", False)

        parent_name = None
        if "parent" in descriptor.fields_by_name:
            parent_field = descriptor.fields_by_name["parent"]
            parent_name = _remove_suffix(parent_field.message_type.name, PROTO_SUFFIX)

        own_fields = [
            _extract_field_info(field)
            for field in descriptor.fields
            if field.name not in ("parent",) and not field.name.startswith(("__", "_"))
        ]

        for field_info in own_fields:
            if not field_info.get("is_external") and field_info.get("message_type"):
                model_info = _resolve_message_model_info(
                    field_info["message_type_full"], field_info["message_type"], all_messages
                )
                field_info.update(model_info)

        model_name = _remove_suffix(info["name"], PROTO_SUFFIX)

        graph[model_name] = {
            "parent": parent_name,
            "parent_model": info.get("parent_model"),  # Nesting parent (not inheritance)
            "class_name": info.get("class_name"),  # Short name for nested classes
            "module": info["module"],
            "class": cls,
            "proto_name": info.get("proto_name", info["name"]),
            "proto_full_path": info.get("proto_full_path", info.get("proto_name", info["name"])),
            "is_nested": is_nested,
            "own_fields": own_fields,
            "all_fields": None,  # Will be computed later
            "children": [],
            "depth": 0,
        }

    for name, info in graph.items():
        if info["parent"] and info["parent"] in graph:
            graph[info["parent"]]["children"].append(name)

    def compute_depth_and_fields(name: str, visited: set[str]) -> int:
        if name in visited:
            raise ValueError(f"Circular inheritance detected: {name}")

        node = graph[name]
        if node["all_fields"] is not None:
            return node["depth"]

        visited.add(name)

        # Compute parent first
        if node["parent"] and node["parent"] in graph:
            parent_depth = compute_depth_and_fields(node["parent"], visited)
            node["depth"] = parent_depth + 1

            # Inherit parent fields
            parent_fields = graph[node["parent"]]["all_fields"]
            node["all_fields"] = parent_fields + node["own_fields"]
        else:
            node["depth"] = 0
            node["all_fields"] = list(node["own_fields"])

        visited.remove(name)
        return node["depth"]

    print("\nComputing inheritance hierarchy...")
    for name in graph:
        if graph[name]["all_fields"] is None:
            compute_depth_and_fields(name, set())

    print(f"\nFound {len(all_enums)} enum types")

    return graph, all_enums


def _escape_reserved_keyword(name: str) -> str:
    """Escape Python reserved keywords by adding underscore suffix"""
    return f"{name}_" if name in RESERVED_KEYWORDS else name


def _get_enum_type_hint(field_info: dict[str, Any]) -> str:
    """Get type hint for enum field"""
    enum_type_name = field_info.get("enum_type_name")
    enum_parent_msg = field_info.get("enum_parent_message")

    if not enum_type_name:
        return "int"

    if enum_parent_msg:
        parent_clean = _remove_suffix(enum_parent_msg, PROTO_SUFFIX)
        return f"'{parent_clean}.{enum_type_name}'"
    return f"'{enum_type_name}'"


def _get_map_type_hint(field_info: dict[str, Any], graph: dict[str, Any] | None) -> str:
    """Get type hint for map field"""
    key_type = field_info.get("map_key_type")
    value_type = field_info.get("map_value_type")

    key_type_str = PROTO_TO_PYTHON_TYPES.get(key_type, "str")

    if value_type == descriptor.FieldDescriptor.TYPE_MESSAGE:
        value_msg_full = field_info.get("map_value_message_full", "")
        value_msg_name = field_info.get("map_value_message_type", "")

        value_model_name = None
        if graph:
            for msg_name, msg_info in graph.items():
                if msg_info.get("proto_full_path") == value_msg_full:
                    value_model_name = msg_info.get("class_name") or msg_name
                    if msg_info.get("is_nested") and msg_info.get("parent_model"):
                        parent_model = msg_info["parent_model"]
                        parent_class = graph[parent_model].get("class_name") or parent_model
                        value_model_name = f"'{parent_class}.{value_model_name}'"
                    else:
                        value_model_name = f"'{value_model_name}'"
                    break

        if not value_model_name:
            value_model_name = f"'{_remove_suffix(value_msg_name, PROTO_SUFFIX)}'"

        value_type_str = value_model_name
    else:
        value_type_str = PROTO_TO_PYTHON_TYPES.get(value_type, "Any")

    return f"Dict[{key_type_str}, {value_type_str}]"


def _get_message_type_hint(field_info: dict[str, Any], graph: dict[str, Any] | None) -> str:
    """Get type hint for message field"""
    is_external = field_info.get("is_external", False)

    if is_external:
        convert_info = field_info.get("convert_to_python")
        if convert_info:
            py_module, py_type, _ = convert_info
            return f"{py_module}.{py_type}"

        external_module = field_info.get("external_module", "")
        external_type = field_info.get("external_type", "")
        if external_module and external_type:
            module_alias = external_module.split(".")[-1]
            return f"{module_alias}.{external_type}"
        return "Any"

    model_name = field_info.get("model_name")
    if model_name and model_name.startswith("Any") and graph and (base_class_name := model_name[3:]) in graph:
        model_name = base_class_name

    if not model_name:
        proto_type = field_info.get("message_type", "Any")
        return f"'{_remove_suffix(proto_type, PROTO_SUFFIX)}'"

    if graph and model_name in graph:
        model_info = graph[model_name]
        if model_info.get("is_nested") and model_info.get("parent_model"):
            path_parts = [model_info.get("class_name") or model_name]
            current = model_name
            while graph[current].get("parent_model"):
                parent = graph[current]["parent_model"]
                if parent in graph:
                    parent_class_name = graph[parent].get("class_name") or parent
                    path_parts.insert(0, parent_class_name)
                else:
                    path_parts.insert(0, parent)
                if parent not in graph or not graph[parent].get("parent_model"):
                    break
                current = parent
            return f"'{'.'.join(path_parts)}'"

    return f"'{model_name}'"


def map_proto_type_to_python(field_info: dict[str, Any], graph: dict[str, Any] | None = None) -> str:
    """Convert protobuf field type to Python type hint for dataclass fields"""
    field_type = field_info["type"]

    if field_type == descriptor.FieldDescriptor.TYPE_ENUM:
        base_type = _get_enum_type_hint(field_info)
        if field_info.get("is_repeated", False):
            return f"List[{base_type}]"
        return f"Optional[{base_type}]"

    if field_info.get("is_map_field", False):
        return _get_map_type_hint(field_info, graph)

    if field_type == descriptor.FieldDescriptor.TYPE_MESSAGE:
        base_type = _get_message_type_hint(field_info, graph)
    else:
        base_type = PROTO_TO_PYTHON_TYPES.get(field_type, "Any")

    if field_info.get("is_repeated", False):
        return f"List[{base_type}]"

    return f"Optional[{base_type}]"


def get_field_default_value(field_info: dict[str, Any]) -> str:
    """Get default value for a dataclass field based on proto field type"""
    if field_info.get("is_map_field", False):
        return "field(default_factory=dict)"
    if field_info.get("is_repeated", False):
        return "field(default_factory=list)"
    return "None"


def scan_available_mixins(mixins_dir: Path) -> set[str]:
    """Scan mixins directory to find available mixin classes"""
    available_mixins = set()

    if not mixins_dir.exists():
        return available_mixins

    for py_file in mixins_dir.glob("*.py"):
        if py_file.name == "__init__.py":
            continue

        try:
            with open(py_file) as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and node.name.endswith(MIXIN_SUFFIX):
                    available_mixins.add(node.name)
        except Exception:
            continue

    return available_mixins


def generate_enum_class(
    enum_name: str,
    enum_info: dict[str, Any],
    module_aliases: dict[str, str],
    available_mixins: set[str],
    indent: int = 0,
) -> str:
    """Generate an IntEnum class for a protobuf enum"""
    lines = []
    indent_str = "    " * indent

    module_alias = module_aliases.get(enum_info["module"], enum_info["module"].split(".")[-1])

    bases = []
    mixin_name = f"{enum_name}{MIXIN_SUFFIX}"
    if mixin_name in available_mixins:
        bases.append(f"proto_model_mixins.{mixin_name}")
    bases.append("IntEnum")

    lines.append(f"{indent_str}class {enum_name}({', '.join(bases)}):")
    lines.append(f'{indent_str}    """')
    lines.append(f"{indent_str}    Auto-generated IntEnum for protobuf {enum_name}.")
    lines.append(f"{indent_str}    ")
    lines.append(f"{indent_str}    Values are directly compatible with protobuf integer constants.")
    lines.append(f'{indent_str}    """')
    lines.append("")

    sorted_values = sorted(enum_info["values"].items(), key=lambda x: x[1])

    parent_msg = enum_info.get("parent_message")
    parent_proto_class = enum_info.get("parent_proto_class")
    if parent_msg and parent_proto_class:
        for value_name, value_number in sorted_values:
            lines.append(
                f"{indent_str}    {value_name} = {module_alias}.{parent_proto_class}.{value_name}  # {value_number}"
            )
    else:
        for value_name, value_number in sorted_values:
            lines.append(f"{indent_str}    {value_name} = {module_alias}.{value_name}  # {value_number}")

    return "\n".join(lines)


def generate_dataclass_fields(info: dict[str, Any], graph: dict[str, Any]) -> str:
    """Generate dataclass field declarations (own fields only)"""
    if not info["own_fields"]:
        return "    pass"

    lines = []
    for field_info in info["own_fields"]:
        field_name = _escape_reserved_keyword(field_info["name"])
        type_hint = map_proto_type_to_python(field_info, graph)
        default_value = get_field_default_value(field_info)
        lines.append(f"    {field_name}: {type_hint} = {default_value}")

    return "\n".join(lines)


def generate_field_metadata(info: dict[str, Any], graph: dict[str, Any]) -> str:
    """Generate _PROTO_FIELD_MAP metadata (own fields only)"""
    if not info["own_fields"]:
        return ""

    lines = ["    _PROTO_FIELD_MAP: ClassVar[Dict[str, Dict[str, Any]]] = {"]

    for field_info in info["own_fields"]:
        field_name = _escape_reserved_keyword(field_info["name"])
        proto_field = field_info["name"]

        is_message = field_info["type"] == descriptor.FieldDescriptor.TYPE_MESSAGE
        is_repeated = field_info.get("is_repeated", False)
        is_enum = field_info["type"] == descriptor.FieldDescriptor.TYPE_ENUM

        lines.append(f"        '{field_name}': {{")
        lines.append(f"            'proto_field': '{proto_field}',")
        lines.append(f"            'is_message': {is_message},")
        lines.append(f"            'is_repeated': {is_repeated},")

        if is_enum:
            enum_type_name = field_info.get("enum_type_name")
            enum_parent_msg = field_info.get("enum_parent_message")
            lines.append("            'is_enum': True,")
            if enum_type_name:
                lines.append(f"            'enum_type_name': '{enum_type_name}',")
            if enum_parent_msg:
                lines.append(f"            'enum_parent_message': '{enum_parent_msg}',")

        lines.append("        },")

    lines.append("    }")
    return "\n".join(lines)


def generate_property(field_info: dict[str, Any], parent_chain: list[str], graph: dict[str, Any] | None = None) -> str:
    """Generate @cached_property code for a field"""
    field_name = field_info["name"]
    type_hint = map_proto_type_to_python(field_info, graph)
    field_type = field_info["type"]
    is_message = field_type == descriptor.FieldDescriptor.TYPE_MESSAGE
    is_repeated = field_info.get("is_repeated", False)

    is_reserved = field_name in RESERVED_KEYWORDS
    method_name = _escape_reserved_keyword(field_name)

    if not parent_chain:
        access_path = f"getattr(self._proto, '{field_name}')" if is_reserved else f"self._proto.{field_name}"
    else:
        parent_path = ".".join(parent_chain)
        access_path = (
            f"getattr(self._proto.{parent_path}, '{field_name}')"
            if is_reserved
            else f"self._proto.{parent_path}.{field_name}"
        )

    doc = f"Field {field_name}"
    if method_name != field_name:
        doc += f" (escaped from reserved keyword '{field_name}')"

    if is_message:
        is_external = field_info.get("is_external", False)

        if is_external:
            convert_info = field_info.get("convert_to_python")
            if convert_info:
                _, _, conversion_method = convert_info
                return_stmt = (
                    f"[item.{conversion_method}() for item in {access_path}]"
                    if is_repeated
                    else f"{access_path}.{conversion_method}() if {access_path}.ByteSize() > 0 else None"
                )
            else:
                return_stmt = (
                    f"list({access_path})"
                    if is_repeated
                    else f"{access_path} if {access_path}.ByteSize() > 0 else None"
                )
        else:
            return_stmt = (
                f"[parse_proto(item) for item in {access_path}]"
                if is_repeated
                else f"parse_proto({access_path}) if {access_path}.ByteSize() > 0 else None"
            )
    else:
        return_stmt = access_path

    return f'''    @cached_property
    def {method_name}(self) -> {type_hint}:
        """{doc}"""
        return {return_stmt}
'''


def generate_class(
    name: str,
    info: dict[str, Any],
    graph: dict[str, Any],
    module_aliases: dict[str, str] | None = None,
    available_mixins: set[str] | None = None,
    indent: int = 0,
    nested_enums: dict[str, list] | None = None,
) -> str:
    """Generate a dataclass-based wrapper class with support for nested classes and enums"""
    if available_mixins is None:
        available_mixins = set()

    parent_name = info["parent"]
    proto_name = info.get("proto_name", name)
    module_name = info["module"]
    is_nested = info.get("is_nested", False)

    class_name = info.get("class_name", name) if is_nested else name

    indent_str = "    " * indent

    bases = []
    mixin_name = f"{class_name}{MIXIN_SUFFIX}"
    if mixin_name in available_mixins:
        bases.append(f"proto_model_mixins.{mixin_name}")

    if parent_name and parent_name in graph:
        bases.append(_remove_suffix(parent_name, PROTO_SUFFIX))
    else:
        bases.append("ProtoModel")

    bases_str = ", ".join(bases)
    class_decl = f"{indent_str}@dataclass\n{indent_str}class {class_name}({bases_str}):"
    docstring = f'{indent_str}    """Generated model for {proto_name}"""'

    parts = [class_decl, docstring]

    if nested_enums and class_name in nested_enums:
        parts.append("")
        parts.append(f"{indent_str}    # Nested Enums")
        for enum_name, enum_info in nested_enums[class_name]:
            enum_code = generate_enum_class(enum_name, enum_info, module_aliases, available_mixins, indent=indent + 1)
            parts.append(enum_code)
            parts.append("")

    fields_code = generate_dataclass_fields(info, graph)
    if fields_code:
        fields_lines = fields_code.split("\n")
        fields_code = "\n".join(indent_str + line if line.strip() else line for line in fields_lines)

    proto_full_path = info.get("proto_full_path", proto_name)

    if module_aliases and module_name in module_aliases:
        module_alias = module_aliases[module_name]
    else:
        module_alias = module_name.split(".")[-1]

    if is_nested and "." in proto_full_path:
        if info.get("parent_model"):
            path_parts = [proto_name]
            current_model = info["parent_model"]

            while current_model:
                if current_model in graph:
                    parent_info = graph[current_model]
                    parent_proto_name = parent_info.get("proto_name", current_model)
                    if "." in parent_proto_name:
                        parent_proto_name = parent_proto_name.split(".")[-1]
                    path_parts.insert(0, parent_proto_name)
                    current_model = parent_info.get("parent_model")
                else:
                    break

            proto_class_ref = f"{module_alias}.{'.'.join(path_parts)}"
        else:
            proto_class_ref = f"{module_alias}.{proto_name}"
    else:
        proto_class_ref = f"{module_alias}.{proto_name}"

    proto_class_line = f"{indent_str}    _PROTO_CLASS: ClassVar[type] = {proto_class_ref}"

    metadata_code = generate_field_metadata(info, graph)
    if metadata_code:
        metadata_lines = metadata_code.split("\n")
        metadata_code = "\n".join(indent_str + line if line.strip() else line for line in metadata_lines)

    indented_pass = f"{indent_str}    pass"
    if fields_code and fields_code.strip() != indented_pass.strip():
        parts.append("")
        parts.append(fields_code)

    parts.append("")
    parts.append(proto_class_line)

    if metadata_code:
        parts.append(metadata_code)
    else:
        parts.append(f"{indent_str}    _PROTO_FIELD_MAP: ClassVar[Dict[str, Dict[str, Any]]] = {{}}")

    return "\n".join(parts)


def generate_model_file(graph: dict[str, Any], enums: dict[str, Any], output_path: Path) -> None:
    """Generate complete proto models Python file with enum types"""
    print(f"\nGenerating proto models file: {output_path}")

    mixins_dir = output_path.parent / "mixins"
    available_mixins = scan_available_mixins(mixins_dir)
    if available_mixins:
        print(f"Found {len(available_mixins)} mixin classes: {', '.join(sorted(available_mixins))}")
    else:
        print("No mixin classes found")

    proto_types_by_module = defaultdict(set)
    external_modules = set()

    for name, info in graph.items():
        proto_types_by_module[info["module"]].add(name)

        for field in info.get("all_fields", []):
            if field.get("is_external") and field.get("external_module"):
                external_modules.add(field["external_module"])

    for enum_name, enum_info in enums.items():
        proto_types_by_module[enum_info["module"]].add(enum_name)

    lines = [
        '"""',
        "ZetaSQL Proto Models",
        "",
        "Auto-generated dataclass-based proto model classes.",
        "DO NOT EDIT MANUALLY - regenerate with scripts/generate_proto_models.py",
        "",
        "Features:",
        "- Dataclass-based concrete models (not proto wrappers)",
        "- Direct instance creation without proto",
        "- Bidirectional proto conversion (from_proto/to_proto)",
        "- MRO-based automatic parent chain tracking",
        "",
        "Usage:",
        "    from zetasql.types import ResolvedLiteral, Type",
        "    ",
        "    # Create instance directly",
        "    literal = ResolvedLiteral(",
        "        value=ValueWithType(...),",
        "        type=Type(type_kind=2),",
        "        has_explicit_type=True",
        "    )",
        "    ",
        "    # Convert to proto",
        "    proto = literal.to_proto()",
        "    ",
        "    # Load from proto",
        "    literal2 = ResolvedLiteral.from_proto(proto)",
        '"""',
        "",
        "from __future__ import annotations",
        "from dataclasses import dataclass, field",
        "from typing import Optional, List, Any, ClassVar, Dict, TYPE_CHECKING",
        "import datetime",
        "",
    ]

    module_aliases = {}
    for module_path in sorted(proto_types_by_module.keys()):
        parts = module_path.split(".")
        alias = f"{parts[-2]}_{parts[-1]}" if len(parts) >= 2 else parts[-1]

        original_alias = alias
        counter = 1
        while alias in module_aliases.values():
            alias = f"{parts[-3]}_{parts[-2]}_{parts[-1]}" if len(parts) >= 3 else f"{original_alias}_{counter}"
            counter += 1

        module_aliases[module_path] = alias
        lines.append(f"import {module_path} as {alias}")

    for external_module in sorted(external_modules):
        alias = external_module.split(".")[-1]
        lines.append(f"import {external_module} as {alias}")

    lines.extend(["", ""])

    lines.extend(
        [
            "# Import IntEnum for enum types",
            "from enum import IntEnum",
            "",
        ]
    )

    lines.extend(
        [
            "# Import utilities for proto model functionality",
            "import zetasql.types.proto_model.mixins as proto_model_mixins",
            "from zetasql.types.proto_model.proto_model import ProtoModel",
            "",
        ]
    )

    root_messages = {}
    children_map = {}

    for name, info in graph.items():
        parent_model = info.get("parent_model")
        if parent_model:
            if parent_model not in children_map:
                children_map[parent_model] = []
            children_map[parent_model].append(name)
        else:
            root_messages[name] = info

    def generate_class_tree(name: str, indent: int = 0) -> str:
        """Generate a class and its nested children recursively"""
        info = graph[name]
        lines = []

        class_code = generate_class(name, info, graph, module_aliases, available_mixins, indent, nested_enums)
        lines.append(class_code)

        if name in children_map:
            for child_name in sorted(children_map[name]):
                lines.append("")
                child_code = generate_class_tree(child_name, indent + 1)
                lines.append(child_code)

        return "\n".join(lines)

    enum_names = []
    top_level_enums = {}
    nested_enums = {}

    if enums:
        for enum_full_name, enum_info in enums.items():
            if enum_info.get("parent_message"):
                parent_msg = enum_info["parent_message"]
                if parent_msg not in nested_enums:
                    nested_enums[parent_msg] = []
                nested_enums[parent_msg].append((enum_info["name"], enum_info))
            else:
                top_level_enums[enum_full_name] = enum_info

        if top_level_enums:
            lines.append("# " + "=" * 76)
            lines.append("# Top-Level Enum Types")
            lines.append("# " + "=" * 76)
            lines.append("")

            for enum_name in sorted(top_level_enums.keys()):
                enum_info = top_level_enums[enum_name]
                enum_code = generate_enum_class(enum_name, enum_info, module_aliases, available_mixins)
                lines.append(enum_code)
                lines.append("\n")
                enum_names.append(enum_name)

            print(f"Generated {len(enum_names)} top-level enum types")

        if nested_enums:
            print(f"Found {sum(len(v) for v in nested_enums.values())} nested enum types")

        lines.append("")
        lines.append("# " + "=" * 76)
        lines.append("# Proto Model Classes")
        lines.append("# " + "=" * 76)
        lines.append("")

    class_count = 0
    class_names = []
    for name in sorted(root_messages.keys(), key=lambda n: (graph[n]["depth"], n)):
        class_code = generate_class_tree(name, indent=0)
        lines.append(class_code)
        lines.append("\n")
        class_count += 1
        class_names.append(name)
        if name in children_map:
            class_count += len(children_map[name])

    export_names = enum_names + class_names
    lines.append("# Export all generated types")
    lines.append("__all__ = [")
    for name in export_names:
        lines.append(f"    '{name}',")
    lines.append("]")
    lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_content = "\n".join(lines)
    output_path.write_text(output_content)

    print(f"Generated {class_count} wrapper classes and {len(enum_names)} enum types")
    print(f"Wrote {len(output_content)} characters to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate ZetaSQL Python wrappers")
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=Path(__file__).parent.parent / "src/zetasql/wasi/_pb2",
        help="Base directory containing _pb2.py files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent.parent / "src/zetasql/types/proto_model/generated.py",
        help="Output Python file",
    )

    args = parser.parse_args()

    if not args.base_dir.exists():
        print(f"Error: Base directory not found: {args.base_dir}")
        sys.exit(1)

    print("=" * 70)
    print("ZetaSQL Python Proto Model Generator")
    print("=" * 70)

    # Extract inheritance graph and enums
    graph, enums = extract_inheritance_graph(args.base_dir)

    # Generate proto models file
    generate_model_file(graph, enums, args.output)

    print("\n" + "=" * 70)
    print("Generation complete!")
    print("=" * 70)
    print(f"\nGenerated file: {args.output}")
    print("\nYou can now use:")
    print("  from zetasql.types import ResolvedLiteral, ASTNode, AnalyzeRequest")
    print("  from zetasql.types import TypeKind, NameResolutionMode, ProductMode")


if __name__ == "__main__":
    main()
