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
from typing import Dict, List, Any, Optional, Set, Tuple
from collections import defaultdict
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


def extract_inheritance_graph(base_dir: Path) -> Dict[str, Any]:
    """
    Extract complete inheritance graph from all _pb2.py files
    
    Returns:
        Dict mapping message names to their metadata:
        {
            'ResolvedLiteralProto': {
                'parent': 'ResolvedExprProto',
                'module': 'zetasql.wasi._pb2.zetasql.resolved_ast.resolved_ast_pb2',
                'class': <class>,
                'own_fields': [...],
                'all_fields': [...],  # including inherited
                'children': [...]
            }
        }
    """
    print(f"Scanning {base_dir} for _pb2.py files...")
    
    # Stage 1: Collect all message classes (including nested)
    all_messages = {}
    module_cache = {}
    
    def collect_nested_messages(descriptor, parent_cls, parent_name, module_name):
        """Recursively collect nested message types"""
        nested_messages = {}
        for nested_type in descriptor.nested_types:
            # Nested wrapper class name: ParentName + NestedName (without 'Proto' suffix)
            nested_model_name = parent_name + nested_type.name.replace('Proto', '')
            nested_proto_full_path = f"{parent_cls.__name__}.{nested_type.name}"
            
            # Get the nested class from parent
            nested_cls = getattr(parent_cls, nested_type.name)
            
            nested_messages[nested_model_name] = {
                'class': nested_cls,
                'module': module_name,
                'name': nested_model_name,
                'proto_name': nested_type.name,
                'proto_full_path': nested_proto_full_path,
                'parent_model': parent_name,
                'is_nested': True
            }
            
            # Recursively collect nested messages within this nested message
            sub_nested = collect_nested_messages(nested_type, nested_cls, nested_model_name, module_name)
            nested_messages.update(sub_nested)
        
        return nested_messages
    
    for pb2_file in sorted(base_dir.rglob('*_pb2.py')):
        if '__pycache__' in str(pb2_file):
            continue
        
        print(f"  Loading {pb2_file.relative_to(base_dir)}...")
        try:
            module = load_pb2_module(pb2_file, base_dir)
            module_cache[pb2_file] = module
            
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
                
                # Collect nested messages
                nested = collect_nested_messages(cls.DESCRIPTOR, cls, name.replace('Proto', ''), module.__name__)
                all_messages.update(nested)
                
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
            parent_name = parent_msg_type.name.replace('Proto', '') if parent_msg_type.name.endswith('Proto') else parent_msg_type.name
        
        # Extract own fields (excluding parent)
        own_fields = []
        for field in descriptor.fields:
            if field.name == 'parent':
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
                            model_name = msg_info['name'].replace('Proto', '') if msg_info['name'].endswith('Proto') else msg_info['name']
                            module_path = msg_info['module']
                            proto_full_path = msg_info.get('proto_full_path', msg_type_name)
                            break
                    
                    if model_name:
                        field_info['model_name'] = model_name
                        field_info['module_path'] = module_path
                        field_info['proto_full_path'] = proto_full_path
            
            own_fields.append(field_info)
        
        model_name = info['name'].replace('Proto', '') if info['name'].endswith('Proto') else info['name']
        
        graph[model_name] = {
            'parent': parent_name,
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
    
    return graph


def map_proto_type_to_python(field_info: Dict[str, Any], graph: Dict[str, Any] = None) -> str:
    """Convert protobuf field type to Python type hint"""
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
    
    # Message type - use Proto type with module prefix
    if field_type == descriptor.FieldDescriptor.TYPE_MESSAGE:
        # Check if this is an external type (e.g., google.protobuf)
        is_external = field_info.get('is_external', False)
        
        if is_external:
            # Check if convertible to Python native type
            convert_info = field_info.get('convert_to_python')
            if convert_info:
                # Use Python native type (e.g., datetime.datetime, datetime.timedelta)
                py_module, py_type, _ = convert_info
                base_type = f"'{py_module}.{py_type}'"
            else:
                # For external types, use the module reference
                external_module = field_info.get('external_module', '')
                external_type = field_info.get('external_type', '')
                if external_module and external_type:
                    # e.g., 'descriptor_pb2.FileDescriptorSet'
                    module_alias = external_module.split('.')[-1]  # 'descriptor_pb2'
                    base_type = f"'{module_alias}.{external_type}'"
                else:
                    base_type = 'Any'
        else:
            # Use model_name if available (handles nested types correctly)
            model_name = field_info.get('model_name')
            proto_full_path = field_info.get('proto_full_path')
            module_path = field_info.get('module_path', '')
            
            # Check if this is a oneof union type (starts with "Any")
            # If so, try to use the base class instead for more accurate type hints
            if model_name and model_name.startswith('Any') and graph:
                # Try to find base class (e.g., AnyResolvedExpr -> ResolvedExpr)
                base_class_name = model_name[3:]  # Remove "Any" prefix
                if base_class_name in graph:
                    # Base class exists, use it for type hint
                    model_name = base_class_name
                    # Also update proto_full_path for the base class
                    if graph[base_class_name].get('proto_full_path'):
                        proto_full_path = graph[base_class_name]['proto_full_path']
                # else: base class doesn't exist, keep original Any* name (fallback)
            
            if model_name and module_path and proto_full_path:
                module_alias = module_path.split('.')[-1]  # e.g., 'resolved_ast_pb2'
                # Use proto_full_path for nested types (e.g., 'AllowedHintsAndOptionsProto.HintProto')
                base_type = f"'{module_alias}.{proto_full_path}'"
            elif model_name:
                # Fallback to wrapper name without module
                base_type = f"'{model_name}'"
            else:
                # Last resort fallback
                proto_type = field_info.get('message_type', 'Any')
                model_type = proto_type.replace('Proto', '') if proto_type.endswith('Proto') else proto_type
                base_type = f"'{model_type}'"
    else:
        base_type = type_map.get(field_type, 'Any')
    
    # Handle repeated fields
    if field_info.get('is_repeated', False):
        return f"List[{base_type}]"
    
    # Optional fields (proto3 all fields are optional)
    return f"Optional[{base_type}]"


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
                model_name = proto_type.replace('Proto', '') if proto_type.endswith('Proto') else proto_type
            
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

def generate_class(name: str, info: Dict[str, Any], graph: Dict[str, Any]) -> str:
    """Generate a single wrapper class"""
    parent_name = info['parent']
    proto_name = info.get('proto_name', name)
    proto_full_path = info.get('proto_full_path', proto_name)
    
    # Determine parent class
    if parent_name and parent_name in graph:
        parent_model = parent_name.replace('Proto', '')
        class_decl = f"class {name}({parent_model}):"
    else:
        # All root classes inherit from ProtoModel
        class_decl = f"class {name}(ProtoModel):"
    
    # Generate properties for ALL fields (own + inherited)
    # Note: No __init__ method - instances are created via from_proto() classmethod
    # Inherited fields need parent chain to access
    properties = []
    
    # Build parent chain for inherited fields
    parent_chain = []
    if parent_name and parent_name in graph:
        current = parent_name
        while current and current in graph:
            parent_chain.insert(0, 'parent')
            current = graph[current]['parent']
    
    # First generate inherited fields with parent chain
    if parent_name and parent_name in graph:
        inherited_fields = graph[parent_name]['all_fields']
        for field in inherited_fields:
            # Calculate proper parent chain depth for this field
            # Find which ancestor owns this field
            ancestor = parent_name
            chain = ['parent']
            
            while ancestor and ancestor in graph:
                if field in graph[ancestor]['own_fields']:
                    # Found the owner
                    break
                ancestor = graph[ancestor]['parent']
                if ancestor and ancestor in graph:
                    chain.insert(0, 'parent')
            
            prop = generate_property(field, chain, graph)
            properties.append(prop)
    
    # Then generate own fields (no parent chain)
    for field in info['own_fields']:
        prop = generate_property(field, [], graph)
        properties.append(prop)
    
    # Combine all parts
    parts = [
        class_decl,
        f'    """Generated model for {proto_name}"""'
    ]
    
    if properties:
        parts.append('')
        parts.extend(properties)
    
    return '\n'.join(parts)


def generate_model_file(graph: Dict[str, Any], output_path: Path) -> None:
    """Generate complete proto models Python file"""
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
    
    # Generate header
    lines = [
        '"""',
        'ZetaSQL Proto Models',
        '',
        'Auto-generated proto model classes for convenient proto field access.',
        'DO NOT EDIT MANUALLY - regenerate with scripts/generate_proto_models.py',
        '',
        'Usage:',
        '    from zetasql.types import ResolvedLiteral, ASTNode, AnalyzeRequest',
        '    ',
        '    proto = resolved_ast_pb2.ResolvedLiteralProto()',
        '    model = ResolvedLiteral.from_proto(proto)',
        '    ',
        '    # Convenient access with IDE autocompletion',
        '    print(model.value)  # Instead of proto.value',
        '    print(model.type)   # Instead of proto.parent.type',
        '"""',
        '',
        'from __future__ import annotations',
        'from functools import cached_property',
        'from typing import Optional, List, Any, TYPE_CHECKING',
        'import datetime',
        '',
        'if TYPE_CHECKING:',
    ]
    
    # Add proto module imports for TYPE_CHECKING
    # Create short alias for each module (e.g., parse_tree_pb2, resolved_ast_pb2)
    for module_path in sorted(proto_types_by_module.keys()):
        # Extract the last part as alias (e.g., 'resolved_ast_pb2' from 'zetasql.wasi._pb2.zetasql.resolved_ast.resolved_ast_pb2')
        module_alias = module_path.split('.')[-1]
        lines.append(f'    import {module_path} as {module_alias}')
    
    # Add external module imports (e.g., google.protobuf)
    for external_module in sorted(external_modules):
        module_alias = external_module.split('.')[-1]
        lines.append(f'    from {external_module} import {module_alias}')
    
    lines.extend(['', ''])
    
    # Import ProtoModel and parse_proto from proto_model
    lines.extend([
        '# Import utilities for proto model functionality',
        'from zetasql.types.proto_model import ProtoModel, parse_proto',
        '',
        '',
    ])
    
    # Generate classes
    class_count = 0
    class_names = []
    for name in sorted_names:
        info = graph[name]
        class_code = generate_class(name, info, graph)
        lines.append(class_code)
        lines.append('\n')
        class_count += 1
        class_names.append(name)
    
    # Generate __all__ for proper exports
    lines.append('# Export all generated proto model classes')
    lines.append('__all__ = [')
    for name in class_names:
        lines.append(f"    '{name}',")
    lines.append(']')
    lines.append('')
    
    # Write file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(lines))
    
    print(f"Generated {class_count} wrapper classes")
    print(f"Wrote {len('\n'.join(lines))} characters to {output_path}")


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
    
    # Extract inheritance graph
    graph = extract_inheritance_graph(args.base_dir)
    
    # Generate proto models file
    generate_model_file(graph, args.output)
    
    print("\n" + "=" * 70)
    print("Generation complete!")
    print("=" * 70)
    print(f"\nGenerated file: {args.output}")
    print("\nYou can now use:")
    print("  from zetasql.types import ResolvedLiteral, ASTNode, AnalyzeRequest")


if __name__ == '__main__':
    main()
