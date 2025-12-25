#!/usr/bin/env python3
"""
ZetaSQL Proto Model Generator

Generates Python proto model classes for ZetaSQL proto messages with:
- Automatic inheritance hierarchy from proto parent fields
- Type hints for IDE autocompletion
- Cached properties for efficient field access
- Cross-file dependency resolution

Usage:
    python scripts/generate_proto_models.py
"""

import sys
import importlib.util
from pathlib import Path
from typing import Dict, List, Any, Set, Tuple
from zetasql.types import proto_model_mixins
import argparse


def load_pb2_module(path: Path, base_dir: Path):
    """Dynamically load a _pb2.py module"""
    # Calculate the module name based on the relative path
    # e.g., base_dir/zetasql/resolved_ast/resolved_ast_pb2.py
    # -> zetasql.wasi._pb2.zetasql.resolved_ast.resolved_ast_pb2
    rel_path = path.relative_to(base_dir)
    module_parts = list(rel_path.parts[:-1]) + [path.stem]  # Remove .py extension
    module_name = 'zetasql.wasi._pb2.' + '.'.join(module_parts)
    
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_message_classes(module) -> List[Tuple[str, Any]]:
    """Extract all proto message classes from a module"""
    classes = []
    for name in dir(module):
        # Skip private/special attributes
        if name.startswith('_'):
            continue
        
        obj = getattr(module, name)
        # Check if it's a proto message class (has DESCRIPTOR with fields)
        if hasattr(obj, 'DESCRIPTOR') and hasattr(obj.DESCRIPTOR, 'fields'):
            classes.append((name, obj))
    
    return classes


def get_enum_types(module) -> List[Tuple[str, Any]]:
    """Extract all proto enum types from a module"""
    enums = []
    for name in dir(module):
        # Skip private/special attributes
        if name.startswith('_'):
            continue
        
        obj = getattr(module, name)
        # Check if it's an enum type wrapper (EnumTypeWrapper with DESCRIPTOR)
        if (hasattr(obj, 'DESCRIPTOR') and 
            hasattr(obj.DESCRIPTOR, 'values') and
            type(obj).__name__ == 'EnumTypeWrapper'):
            enums.append((name, obj))
    
    return enums


def extract_inheritance_graph(base_dir: Path) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Extract complete inheritance graph and enums from all _pb2.py files
    
    Returns:
        Tuple of (graph, enums):
        - graph: Dict mapping message names to their metadata
        - enums: Dict mapping enum names to their metadata
    """
    print(f"Scanning {base_dir} for _pb2.py files...")
    
    # Stage 1: Collect all message classes (including nested) and enums
    all_messages = {}
    all_enums = {}
    module_cache = {}
    
    def collect_nested_messages(descriptor, parent_cls, parent_name, module_name, parent_proto_path=""):
        """Recursively collect nested message types"""
        nested_messages = {}
        for nested_type in descriptor.nested_types:
            # Full model name for graph key (flat compatibility): ParentName + NestedName
            nested_full_model_name = parent_name + nested_type.name.removesuffix('Proto')
            
            # Short class name for actual nested class: just NestedName without Proto suffix
            nested_class_name = nested_type.name.removesuffix('Proto')
            
            # Build full proto path for nested types
            # parent_proto_path: "ScriptExecutorStateProto" or "ScriptExecutorStateProto.StackFrame"
            # nested_type.name: "StackFrame" or "Parameters"
            if parent_proto_path:
                nested_proto_full_path = f"{parent_proto_path}.{nested_type.name}"
            else:
                nested_proto_full_path = f"{parent_cls.__name__}.{nested_type.name}"
            
            # Get the nested class from parent
            nested_cls = getattr(parent_cls, nested_type.name)
            
            # Use full name as key for graph (flat compatibility)
            # but store the short class name for code generation
            nested_messages[nested_full_model_name] = {
                'class': nested_cls,
                'module': module_name,
                'name': nested_full_model_name,  # Full name for graph key
                'class_name': nested_class_name,  # Short name for class definition
                'proto_name': nested_type.name,
                'proto_full_path': nested_proto_full_path,
                'parent_model': parent_name,
                'is_nested': True
            }
            
            # Recursively collect nested messages within this nested message
            # Pass the full path so far, and use full name as parent
            sub_nested = collect_nested_messages(
                nested_type, 
                nested_cls, 
                nested_full_model_name,  # Use full name for next level's parent
                module_name,
                nested_proto_full_path
            )
            nested_messages.update(sub_nested)
        
        return nested_messages
    
    for pb2_file in sorted(base_dir.rglob('*_pb2.py')):
        if '__pycache__' in str(pb2_file):
            continue
        
        print(f"  Loading {pb2_file.relative_to(base_dir)}...")
        try:
            module = load_pb2_module(pb2_file, base_dir)
            module_cache[pb2_file] = module
            
            # Collect message classes
            for name, cls in get_message_classes(module):
                full_name = name
                all_messages[full_name] = {
                    'class': cls,
                    'module': module.__name__,
                    'name': name,
                    'proto_name': name,
                    'file': pb2_file,
                    'is_nested': False
                }
                
                # Collect nested messages - pass parent proto full path
                nested = collect_nested_messages(
                    cls.DESCRIPTOR, 
                    cls, 
                    name.removesuffix('Proto'), 
                    module.__name__,
                    name  # Parent proto path (e.g., "ScriptExecutorStateProto")
                )
                all_messages.update(nested)
            
            # Collect enum types
            for enum_name, enum_cls in get_enum_types(module):
                all_enums[enum_name] = {
                    'name': enum_name,
                    'class': enum_cls,
                    'module': module.__name__,
                    'file': pb2_file,
                    'values': {}
                }
                
                # Extract enum values from DESCRIPTOR
                for value in enum_cls.DESCRIPTOR.values:
                    all_enums[enum_name]['values'][value.name] = value.number
                
        except Exception as e:
            print(f"  Warning: Failed to load {pb2_file}: {e}")
            continue
    
    print(f"\nFound {len(all_messages)} proto message classes (including nested)")
    
    # Stage 2: Extract parent relationships and fields
    graph = {}
    
    for full_name, info in all_messages.items():
        cls = info['class']
        descriptor = cls.DESCRIPTOR
        is_nested = info.get('is_nested', False)
        
        # Extract parent (for inheritance, not nesting)
        parent_name = None
        if 'parent' in descriptor.fields_by_name:
            parent_field = descriptor.fields_by_name['parent']
            parent_msg_type = parent_field.message_type
            # Remove 'Proto' suffix to match graph keys
            parent_name = parent_msg_type.name.removesuffix('Proto')
        
        # Extract own fields (excluding parent and internal proto fields)
        own_fields = []
        for field in descriptor.fields:
            if field.name == 'parent':
                continue
            
            # Skip internal proto fields (usually start with __)
            if field.name.startswith('__') or field.name.startswith('_'):
                continue
            
            field_info = {
                'name': field.name,
                'type': field.type,
                'is_repeated': field.is_repeated,
                'number': field.number,
            }
            
            # Add message type info if applicable
            if field.message_type:
                msg_type_name = field.message_type.name
                msg_type_full = field.message_type.full_name
                
                field_info['message_type'] = msg_type_name
                field_info['message_type_full'] = msg_type_full
                
                # Check if this is an external type (e.g., google.protobuf)
                is_external = not msg_type_full.startswith('zetasql.')
                field_info['is_external'] = is_external
                
                if is_external:
                    # For external types like google.protobuf, store the module info
                    if msg_type_full.startswith('google.protobuf.'):
                        # Check if this type can be converted to Python native type
                        # Format: proto_type_name -> (python_module, python_type, conversion_method)
                        convertible_types = {
                            'Timestamp': ('datetime', 'datetime', 'ToDatetime'),
                            'Duration': ('datetime', 'timedelta', 'ToTimedelta'),
                        }
                        
                        if msg_type_name in convertible_types:
                            # Mark as convertible to Python native type
                            field_info['convert_to_python'] = convertible_types[msg_type_name]
                        
                        # Extract module name from full_name (e.g., google.protobuf.FileDescriptorSet -> descriptor_pb2)
                        # Map common google.protobuf types to their pb2 module
                        proto_file = field.message_type.file.name  # e.g., "google/protobuf/descriptor.proto"
                        # Extract just the filename without path and extension, add _pb2
                        proto_filename = proto_file.split('/')[-1].replace('.proto', '')  # "descriptor"
                        proto_module = f"google.protobuf.{proto_filename}_pb2"  # "google.protobuf.descriptor_pb2"
                        field_info['external_module'] = proto_module
                        field_info['external_type'] = msg_type_name
                else:
                    # Find the wrapper name and module for this message type
                    # Check if it's a nested type first (contains dot in full_name after package)
                    model_name = None
                    module_path = None
                    proto_full_path = None
                    
                    # Try to find exact match in all_messages
                    for msg_name, msg_info in all_messages.items():
                        if msg_info.get('proto_name') == msg_type_name or msg_name == msg_type_name:
                            model_name = msg_info['name'].removesuffix('Proto')
                            module_path = msg_info['module']
                            proto_full_path = msg_info.get('proto_full_path', msg_type_name)
                            break
                    
                    if model_name:
                        field_info['model_name'] = model_name
                        field_info['module_path'] = module_path
                        field_info['proto_full_path'] = proto_full_path
            
            own_fields.append(field_info)
        
        model_name = info['name'].removesuffix('Proto')
        
        graph[model_name] = {
            'parent': parent_name,
            'parent_model': info.get('parent_model'),  # Nesting parent (not inheritance)
            'class_name': info.get('class_name'),  # Short name for nested classes
            'module': info['module'],
            'class': cls,
            'proto_name': info.get('proto_name', info['name']),
            'proto_full_path': info.get('proto_full_path', info.get('proto_name', info['name'])),
            'is_nested': is_nested,
            'own_fields': own_fields,
            'all_fields': None,  # Will be computed later
            'children': [],
            'depth': 0
        }
    
    # Stage 3: Build parent-child relationships
    for name, info in graph.items():
        if info['parent'] and info['parent'] in graph:
            graph[info['parent']]['children'].append(name)
    
    # Stage 4: Compute inheritance depth and all fields
    def compute_depth_and_fields(name: str, visited: Set[str]) -> int:
        if name in visited:
            raise ValueError(f"Circular inheritance detected: {name}")
        
        node = graph[name]
        if node['all_fields'] is not None:
            return node['depth']
        
        visited.add(name)
        
        # Compute parent first
        if node['parent'] and node['parent'] in graph:
            parent_depth = compute_depth_and_fields(node['parent'], visited)
            node['depth'] = parent_depth + 1
            
            # Inherit parent fields
            parent_fields = graph[node['parent']]['all_fields']
            node['all_fields'] = parent_fields + node['own_fields']
        else:
            node['depth'] = 0
            node['all_fields'] = list(node['own_fields'])
        
        visited.remove(name)
        return node['depth']
    
    print("\nComputing inheritance hierarchy...")
    for name in graph:
        if graph[name]['all_fields'] is None:
            compute_depth_and_fields(name, set())
    
    print(f"\nFound {len(all_enums)} enum types")
    
    return graph, all_enums


def map_proto_type_to_python(field_info: Dict[str, Any], graph: Dict[str, Any] = None) -> str:
    """Convert protobuf field type to Python type hint for dataclass fields"""
    from google.protobuf import descriptor
    
    type_map = {
        descriptor.FieldDescriptor.TYPE_STRING: 'str',
        descriptor.FieldDescriptor.TYPE_INT64: 'int',
        descriptor.FieldDescriptor.TYPE_INT32: 'int',
        descriptor.FieldDescriptor.TYPE_UINT64: 'int',
        descriptor.FieldDescriptor.TYPE_UINT32: 'int',
        descriptor.FieldDescriptor.TYPE_BOOL: 'bool',
        descriptor.FieldDescriptor.TYPE_DOUBLE: 'float',
        descriptor.FieldDescriptor.TYPE_FLOAT: 'float',
        descriptor.FieldDescriptor.TYPE_BYTES: 'bytes',
        descriptor.FieldDescriptor.TYPE_ENUM: 'int',
    }
    
    field_type = field_info['type']
    
    # Message type
    if field_type == descriptor.FieldDescriptor.TYPE_MESSAGE:
        is_external = field_info.get('is_external', False)
        
        if is_external:
            convert_info = field_info.get('convert_to_python')
            if convert_info:
                py_module, py_type, _ = convert_info
                base_type = f"{py_module}.{py_type}"
            else:
                external_module = field_info.get('external_module', '')
                external_type = field_info.get('external_type', '')
                if external_module and external_type:
                    module_alias = external_module.split('.')[-1]
                    base_type = f"{module_alias}.{external_type}"
                else:
                    base_type = 'Any'
        else:
            model_name = field_info.get('model_name')
            if model_name and model_name.startswith('Any') and graph:
                base_class_name = model_name[3:]
                if base_class_name in graph:
                    model_name = base_class_name
            
            if model_name:
                # Check if this is a nested class by looking at parent_model in graph
                if graph and model_name in graph:
                    model_info = graph[model_name]
                    if model_info.get('is_nested') and model_info.get('parent_model'):
                        # Build full nested path (e.g., 'ScriptExecutorState.StackFrame')
                        parent_model = model_info['parent_model']
                        # Recursively build the path for deeply nested classes
                        path_parts = [model_name]
                        current = model_name
                        while graph[current].get('parent_model'):
                            parent = graph[current]['parent_model']
                            path_parts.insert(0, parent)
                            if parent not in graph or not graph[parent].get('parent_model'):
                                break
                            current = parent
                        base_type = f"'{'.'.join(path_parts)}'"
                    else:
                        base_type = f"'{model_name}'"
                else:
                    base_type = f"'{model_name}'"
            else:
                proto_type = field_info.get('message_type', 'Any')
                model_type = proto_type.removesuffix('Proto')
                base_type = f"'{model_type}'"
    else:
        base_type = type_map.get(field_type, 'Any')
    
    # Handle repeated fields
    if field_info.get('is_repeated', False):
        return f"List[{base_type}]"
    
    # Optional for message types, direct for primitives (with defaults)
    if field_type == descriptor.FieldDescriptor.TYPE_MESSAGE:
        return f"Optional[{base_type}]"
    else:
        return base_type


def get_field_default_value(field_info: Dict[str, Any]) -> str:
    """Get default value for a dataclass field based on proto field type"""
    from google.protobuf import descriptor
    
    if field_info.get('is_repeated', False):
        return "field(default_factory=list)"
    
    field_type = field_info['type']
    
    # Message types default to None
    if field_type == descriptor.FieldDescriptor.TYPE_MESSAGE:
        return "None"
    
    # Primitive types have zero/empty defaults
    default_map = {
        descriptor.FieldDescriptor.TYPE_STRING: '""',
        descriptor.FieldDescriptor.TYPE_INT64: '0',
        descriptor.FieldDescriptor.TYPE_INT32: '0',
        descriptor.FieldDescriptor.TYPE_UINT64: '0',
        descriptor.FieldDescriptor.TYPE_UINT32: '0',
        descriptor.FieldDescriptor.TYPE_BOOL: 'False',
        descriptor.FieldDescriptor.TYPE_DOUBLE: '0.0',
        descriptor.FieldDescriptor.TYPE_FLOAT: '0.0',
        descriptor.FieldDescriptor.TYPE_BYTES: 'b""',
        descriptor.FieldDescriptor.TYPE_ENUM: '0',
    }
    
    return default_map.get(field_type, 'None')


def generate_enum_class(enum_name: str, enum_info: Dict[str, Any], module_aliases: Dict[str, str]) -> str:
    """Generate an IntEnum class for a protobuf enum"""
    lines = []
    
    # Get module alias
    module_path = enum_info['module']
    module_alias = module_aliases.get(module_path, module_path.split('.')[-1])

    bases = []
    mixin_name = f'{enum_name}Mixin'
    if hasattr(proto_model_mixins, mixin_name):
        bases.append(f'proto_model_mixins.{mixin_name}')
    bases.append('IntEnum')

    # Class definition
    lines.append(f"class {enum_name}({', '.join(bases)}):")
    lines.append(f'    """')
    lines.append(f'    Auto-generated IntEnum for protobuf {enum_name}.')
    lines.append(f'    ')
    lines.append(f'    Values are directly compatible with protobuf integer constants.')
    lines.append(f'    """')
    lines.append('')
    
    # Sort values by number for consistent ordering
    sorted_values = sorted(enum_info['values'].items(), key=lambda x: x[1])
    
    # Generate enum members
    for value_name, value_number in sorted_values:
        lines.append(f"    {value_name} = {module_alias}.{value_name}  # {value_number}")
    
    return '\n'.join(lines)


def generate_dataclass_fields(info: Dict[str, Any], graph: Dict[str, Any]) -> str:
    """Generate dataclass field declarations (own fields only)"""
    from google.protobuf import descriptor
    
    if not info['own_fields']:
        return "    pass"
    
    lines = []
    
    for field_info in info['own_fields']:
        field_name = field_info['name']
        
        # Escape reserved keywords
        RESERVED_KEYWORDS = {
            'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
            'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
            'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
            'raise', 'return', 'try', 'while', 'with', 'yield'
        }
        
        if field_name in RESERVED_KEYWORDS:
            field_name = f"{field_name}_"
        
        type_hint = map_proto_type_to_python(field_info, graph)
        default_value = get_field_default_value(field_info)
        
        # Check if we need to import field() for default_factory
        if 'default_factory' in default_value:
            lines.append(f"    {field_name}: {type_hint} = {default_value}")
        else:
            lines.append(f"    {field_name}: {type_hint} = {default_value}")
    
    return '\n'.join(lines)


def generate_field_metadata(info: Dict[str, Any], graph: Dict[str, Any]) -> str:
    """Generate _PROTO_FIELD_MAP metadata (own fields only)"""
    if not info['own_fields']:
        return ""
    
    lines = []
    lines.append("    _PROTO_FIELD_MAP: ClassVar[Dict[str, Dict[str, Any]]] = {")
    
    for field_info in info['own_fields']:
        field_name = field_info['name']
        proto_field = field_name
        
        # Escape reserved keywords
        RESERVED_KEYWORDS = {
            'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
            'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
            'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
            'raise', 'return', 'try', 'while', 'with', 'yield'
        }
        
        if field_name in RESERVED_KEYWORDS:
            field_name = f"{field_name}_"
        
        from google.protobuf import descriptor
        is_message = field_info['type'] == descriptor.FieldDescriptor.TYPE_MESSAGE
        is_repeated = field_info.get('is_repeated', False)
        
        lines.append(f"        '{field_name}': {{")
        lines.append(f"            'proto_field': '{proto_field}',")
        lines.append(f"            'is_message': {is_message},")
        lines.append(f"            'is_repeated': {is_repeated},")
        lines.append(f"        }},")
    
    lines.append("    }")
    
    return '\n'.join(lines)


def generate_property(field_info: Dict[str, Any], parent_chain: List[str], graph: Dict[str, Any] = None) -> str:
    """Generate @cached_property code for a field"""
    from google.protobuf import descriptor
    
    field_name = field_info['name']
    type_hint = map_proto_type_to_python(field_info, graph)
    field_type = field_info['type']
    is_message = field_type == descriptor.FieldDescriptor.TYPE_MESSAGE
    is_repeated = field_info.get('is_repeated', False)
    
    # Python reserved keywords that need to be suffixed
    RESERVED_KEYWORDS = {
        'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
        'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
        'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
        'raise', 'return', 'try', 'while', 'with', 'yield'
    }
    
    # Escape reserved keywords
    is_reserved = field_name in RESERVED_KEYWORDS
    method_name = f"{field_name}_" if is_reserved else field_name
    
    # Build access path - use getattr for reserved keywords
    if not parent_chain:
        if is_reserved:
            access_path = f"getattr(self._proto, '{field_name}')"
        else:
            access_path = f"self._proto.{field_name}"
    else:
        parent_path = '.'.join(parent_chain)
        if is_reserved:
            access_path = f"getattr(self._proto.{parent_path}, '{field_name}')"
        else:
            access_path = f"self._proto.{parent_path}.{field_name}"
    
    # Generate docstring
    doc = f"Field {field_name}"
    if method_name != field_name:
        doc += f" (escaped from reserved keyword '{field_name}')"
    
    # Generate return statement
    if is_message:
        # Check if this is an external type (e.g., google.protobuf)
        is_external = field_info.get('is_external', False)
        
        if is_external:
            # Check if convertible to Python native type
            convert_info = field_info.get('convert_to_python')
            if convert_info:
                # Convert to Python native type
                _, _, conversion_method = convert_info
                
                if is_repeated:
                    return_stmt = f"[item.{conversion_method}() for item in {access_path}]"
                else:
                    return_stmt = f"{access_path}.{conversion_method}() if {access_path}.ByteSize() > 0 else None"
            else:
                # External types: return proto object directly (no wrapper)
                if is_repeated:
                    return_stmt = f"list({access_path})"
                else:
                    return_stmt = f"{access_path} if {access_path}.ByteSize() > 0 else None"
        else:
            # Get wrapper class name (use model_name if available for nested types)
            model_name = field_info.get('model_name')
            if not model_name:
                proto_type = field_info.get('message_type', '')
                model_name = proto_type.removesuffix('Proto')
            
            # Use parse_proto() for all wrapper creation (handles union auto-resolution)
            if is_repeated:
                # Return list of wrapped objects
                return_stmt = f"[parse_proto(item) for item in {access_path}]"
            else:
                # Return wrapped object or None
                return_stmt = f"parse_proto({access_path}) if {access_path}.ByteSize() > 0 else None"
    else:
        # Primitive types - return as-is
        return_stmt = access_path
    
    return f'''    @cached_property
    def {method_name}(self) -> {type_hint}:
        """{doc}"""
        return {return_stmt}
'''

def generate_class(name: str, info: Dict[str, Any], graph: Dict[str, Any], module_aliases: Dict[str, str] = None, indent: int = 0) -> str:
    """Generate a dataclass-based wrapper class with support for nested classes"""
    parent_name = info['parent']
    proto_name = info.get('proto_name', name)
    module_name = info['module']
    is_nested = info.get('is_nested', False)
    
    # Use short class name for nested classes, full name for top-level
    class_name = info.get('class_name', name) if is_nested else name
    
    # Create indentation string
    indent_str = '    ' * indent
    
    # Determine parent class with optional mixin
    bases = []
    mixin_name = f'{class_name}Mixin'
    if hasattr(proto_model_mixins, mixin_name):
        bases.append(f'proto_model_mixins.{mixin_name}')

    if parent_name and parent_name in graph:
        parent_model = parent_name.removesuffix('Proto')
        bases.append(parent_model)
    else:
        # Root classes inherit from ProtoModel
        bases.append("ProtoModel")
    
    bases_str = ", ".join(bases)
    class_decl = f"{indent_str}@dataclass\n{indent_str}class {class_name}({bases_str}):"
    
    # Generate docstring
    docstring = f'{indent_str}    """Generated model for {proto_name}"""'
    
    # Generate dataclass fields (own fields only)
    fields_code = generate_dataclass_fields(info, graph)
    # Apply indentation to fields
    if fields_code:
        fields_lines = fields_code.split('\n')
        fields_code = '\n'.join(indent_str + line if line.strip() else line for line in fields_lines)
    
    # Generate proto class reference
    proto_full_path = info.get('proto_full_path', proto_name)
    
    # Get the module alias from module_aliases map (if provided)
    if module_aliases and module_name in module_aliases:
        module_alias = module_aliases[module_name]
    else:
        # Fallback to last part of module name
        module_alias = module_name.split('.')[-1]
    
    # Direct attribute access for all types (including nested)
    if is_nested and '.' in proto_full_path:
        # Use dot notation: module.Parent.Nested
        proto_class_ref = f"{module_alias}.{proto_full_path}"
    else:
        # Direct attribute access for top-level types
        proto_class_ref = f"{module_alias}.{proto_name}"
    
    proto_class_line = f"{indent_str}    _PROTO_CLASS: ClassVar[type] = {proto_class_ref}"
    
    # Generate metadata
    metadata_code = generate_field_metadata(info, graph)
    # Apply indentation to metadata
    if metadata_code:
        metadata_lines = metadata_code.split('\n')
        metadata_code = '\n'.join(indent_str + line if line.strip() else line for line in metadata_lines)
    
    # Combine all parts
    parts = [class_decl, docstring]
    
    # Add fields
    indented_pass = f"{indent_str}    pass"
    if fields_code and fields_code.strip() != indented_pass.strip():
        parts.append("")
        parts.append(fields_code)
    
    # Add metadata
    parts.append("")
    parts.append(proto_class_line)
    
    if metadata_code:
        parts.append(metadata_code)
    else:
        parts.append(f"{indent_str}    _PROTO_FIELD_MAP: ClassVar[Dict[str, Dict[str, Any]]] = {{}}")
    
    return '\n'.join(parts)


def generate_model_file(graph: Dict[str, Any], enums: Dict[str, Any], output_path: Path) -> None:
    """Generate complete proto models Python file with enum types"""
    print(f"\nGenerating proto models file: {output_path}")
    
    # Sort by depth (parents first)
    sorted_names = sorted(graph.keys(), key=lambda n: (graph[n]['depth'], n))
    
    # Collect all proto types by module for TYPE_CHECKING imports
    from collections import defaultdict
    proto_types_by_module = defaultdict(set)
    external_modules = set()
    
    for name, info in graph.items():
        # Extract module path
        # Module is like: zetasql.wasi._pb2.zetasql.resolved_ast.resolved_ast_pb2
        module_name = info['module']
        proto_types_by_module[module_name].add(name)
        
        # Also collect external modules from fields
        for field in info.get('all_fields', []):
            if field.get('is_external') and field.get('external_module'):
                external_modules.add(field['external_module'])
    
    # Also collect enum modules
    for enum_name, enum_info in enums.items():
        module_name = enum_info['module']
        proto_types_by_module[module_name].add(enum_name)
    
    # Generate header
    lines = [
        '"""',
        'ZetaSQL Proto Models',
        '',
        'Auto-generated dataclass-based proto model classes.',
        'DO NOT EDIT MANUALLY - regenerate with scripts/generate_proto_models.py',
        '',
        'Features:',
        '- Dataclass-based concrete models (not proto wrappers)',
        '- Direct instance creation without proto',
        '- Bidirectional proto conversion (from_proto/to_proto)',
        '- MRO-based automatic parent chain tracking',
        '',
        'Usage:',
        '    from zetasql.types import ResolvedLiteral, Type',
        '    ',
        '    # Create instance directly',
        '    literal = ResolvedLiteral(',
        '        value=ValueWithType(...),',
        '        type=Type(type_kind=2),',
        '        has_explicit_type=True',
        '    )',
        '    ',
        '    # Convert to proto',
        '    proto = literal.to_proto()',
        '    ',
        '    # Load from proto',
        '    literal2 = ResolvedLiteral.from_proto(proto)',
        '"""',
        '',
        'from __future__ import annotations',
        'from dataclasses import dataclass, field',
        'from typing import Optional, List, Any, ClassVar, Dict, TYPE_CHECKING',
        'import datetime',
        '',
    ]
    
    # Add proto module imports (NOT in TYPE_CHECKING - needed at runtime for _PROTO_CLASS)
    # Create UNIQUE alias for each module by including more path context if needed
    module_aliases = {}
    for module_path in sorted(proto_types_by_module.keys()):
        # Extract the last two parts for uniqueness (e.g., 'proto_options_pb2', 'public_options_pb2')
        parts = module_path.split('.')
        if len(parts) >= 2:
            # Use last two parts: e.g., zetasql.proto.options_pb2 -> proto_options_pb2
            alias = f"{parts[-2]}_{parts[-1]}"
        else:
            alias = parts[-1]
        
        # Handle potential collisions by adding more parts
        original_alias = alias
        counter = 1
        while alias in module_aliases.values():
            if len(parts) >= 3:
                alias = f"{parts[-3]}_{parts[-2]}_{parts[-1]}"
            else:
                alias = f"{original_alias}_{counter}"
                counter += 1
        
        module_aliases[module_path] = alias
        lines.append(f'import {module_path} as {alias}')
    
    # Add external module imports
    for external_module in sorted(external_modules):
        # Use short alias: google.protobuf.any_pb2 -> any_pb2
        alias = external_module.split('.')[-1]
        lines.append(f'import {external_module} as {alias}')
    
    lines.extend(['', ''])
    
    # Import IntEnum for enum types
    lines.extend([
        '# Import IntEnum for enum types',
        'from enum import IntEnum',
        '',
    ])
    
    # Import ProtoModel and parse_proto from proto_model
    lines.extend([
        '# Import utilities for proto model functionality',
        'from zetasql.types.proto_model import ProtoModel, parse_proto',
        'from zetasql.types import proto_model_mixins',
        '',
    ])
    
    # Generate classes - pass module_aliases to generate_class
    # Build tree structure for nested classes
    root_messages = {}  # Top-level messages
    children_map = {}   # Map parent -> list of children
    
    for name, info in graph.items():
        parent_model = info.get('parent_model')
        if parent_model:
            # This is a nested class
            if parent_model not in children_map:
                children_map[parent_model] = []
            children_map[parent_model].append(name)
        else:
            # This is a top-level class
            root_messages[name] = info
    
    def generate_class_tree(name: str, indent: int = 0) -> str:
        """Generate a class and its nested children recursively"""
        info = graph[name]
        lines = []
        
        # Generate the class itself
        class_code = generate_class(name, info, graph, module_aliases, indent)
        lines.append(class_code)
        
        # Generate nested children
        if name in children_map:
            for child_name in sorted(children_map[name]):
                lines.append("")  # Blank line between nested classes
                child_code = generate_class_tree(child_name, indent + 1)
                lines.append(child_code)
        
        return '\n'.join(lines)
    
    # Generate enum types first (before classes, so they can be referenced)
    enum_names = []
    if enums:
        lines.append('# ============================================================================')
        lines.append('# Enum Types')
        lines.append('# ============================================================================')
        lines.append('')
        
        for enum_name in sorted(enums.keys()):
            enum_info = enums[enum_name]
            enum_code = generate_enum_class(enum_name, enum_info, module_aliases)
            lines.append(enum_code)
            lines.append('\n')
            enum_names.append(enum_name)
        
        print(f"Generated {len(enum_names)} enum types")
        
        lines.append('')
        lines.append('# ============================================================================')
        lines.append('# Proto Model Classes')
        lines.append('# ============================================================================')
        lines.append('')
    
    # Generate all top-level classes with their nested trees
    class_count = 0
    class_names = []
    for name in sorted(root_messages.keys(), key=lambda n: (graph[n]['depth'], n)):
        info = root_messages[name]
        class_code = generate_class_tree(name, indent=0)
        lines.append(class_code)
        lines.append('\n')
        class_count += 1
        class_names.append(name)
        # Count nested classes too
        if name in children_map:
            class_count += len(children_map[name])
    
    # Generate __all__ for proper exports (enums + classes)
    export_names = ['parse_proto', 'ProtoModel'] + enum_names + class_names
    lines.append('# Export all generated types')
    lines.append('__all__ = [')
    for name in export_names:
        lines.append(f"    '{name}',")
    lines.append(']')
    lines.append('')
    
    # Write file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_content = '\n'.join(lines)
    output_path.write_text(output_content)
    
    print(f"Generated {class_count} wrapper classes and {len(enum_names)} enum types")
    print(f"Wrote {len(output_content)} characters to {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Generate ZetaSQL Python wrappers')
    parser.add_argument(
        '--base-dir',
        type=Path,
        default=Path(__file__).parent.parent / 'src/zetasql/wasi/_pb2',
        help='Base directory containing _pb2.py files'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path(__file__).parent.parent / 'src/zetasql/types/proto_models.py',
        help='Output Python file'
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


if __name__ == '__main__':
    main()
