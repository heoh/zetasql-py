#!/usr/bin/env python3
"""
ZetaSQL ResolvedAST Python Wrapper Generator

Generates Python wrapper classes for ZetaSQL proto messages with:
- Automatic inheritance hierarchy from proto parent fields
- Type hints for IDE autocompletion
- Cached properties for efficient field access
- Cross-file dependency resolution

Usage:
    python scripts/generate_wrappers.py
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
        if name.startswith('Any'):  # Skip oneof wrappers
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
            nested_wrapper_name = parent_name + nested_type.name.replace('Proto', '')
            nested_proto_full_path = f"{parent_cls.__name__}.{nested_type.name}"
            
            # Get the nested class from parent
            nested_cls = getattr(parent_cls, nested_type.name)
            
            nested_messages[nested_wrapper_name] = {
                'class': nested_cls,
                'module': module_name,
                'name': nested_wrapper_name,
                'proto_name': nested_type.name,
                'proto_full_path': nested_proto_full_path,
                'parent_wrapper': parent_name,
                'is_nested': True
            }
            
            # Recursively collect nested messages within this nested message
            sub_nested = collect_nested_messages(nested_type, nested_cls, nested_wrapper_name, module_name)
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
                
                # Find the wrapper name and module for this message type
                # Check if it's a nested type first (contains dot in full_name after package)
                wrapper_name = None
                module_path = None
                proto_full_path = None
                
                # Try to find exact match in all_messages
                for msg_name, msg_info in all_messages.items():
                    if msg_info.get('proto_name') == msg_type_name or msg_name == msg_type_name:
                        wrapper_name = msg_info['name'].replace('Proto', '') if msg_info['name'].endswith('Proto') else msg_info['name']
                        module_path = msg_info['module']
                        proto_full_path = msg_info.get('proto_full_path', msg_type_name)
                        break
                
                if wrapper_name:
                    field_info['wrapper_name'] = wrapper_name
                    field_info['module_path'] = module_path
                    field_info['proto_full_path'] = proto_full_path
            
            own_fields.append(field_info)
        
        wrapper_name = info['name'].replace('Proto', '') if info['name'].endswith('Proto') else info['name']
        
        graph[wrapper_name] = {
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


def map_proto_type_to_python(field_info: Dict[str, Any]) -> str:
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
        # Use wrapper_name if available (handles nested types correctly)
        wrapper_name = field_info.get('wrapper_name')
        proto_full_path = field_info.get('proto_full_path')
        module_path = field_info.get('module_path', '')
        
        if wrapper_name and module_path and proto_full_path:
            module_alias = module_path.split('.')[-1]  # e.g., 'resolved_ast_pb2'
            # Use proto_full_path for nested types (e.g., 'AllowedHintsAndOptionsProto.HintProto')
            base_type = f"'{module_alias}.{proto_full_path}'"
        elif wrapper_name:
            # Fallback to wrapper name without module
            base_type = f"'{wrapper_name}'"
        else:
            # Last resort fallback
            proto_type = field_info.get('message_type', 'Any')
            wrapper_type = proto_type.replace('Proto', '') if proto_type.endswith('Proto') else proto_type
            base_type = f"'{wrapper_type}'"
    else:
        base_type = type_map.get(field_type, 'Any')
    
    # Handle repeated fields
    if field_info.get('is_repeated', False):
        return f"List[{base_type}]"
    
    # Optional fields (proto3 all fields are optional)
    return f"Optional[{base_type}]"


def generate_property(field_info: Dict[str, Any], parent_chain: List[str]) -> str:
    """Generate @cached_property code for a field"""
    from google.protobuf import descriptor
    
    field_name = field_info['name']
    type_hint = map_proto_type_to_python(field_info)
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
        # Get wrapper class name (use wrapper_name if available for nested types)
        wrapper_name = field_info.get('wrapper_name')
        if not wrapper_name:
            proto_type = field_info.get('message_type', '')
            wrapper_name = proto_type.replace('Proto', '') if proto_type.endswith('Proto') else proto_type
        
        if is_repeated:
            # Return list of wrapped objects
            return_stmt = f"[{wrapper_name}(item) for item in {access_path}]"
        else:
            # Return wrapped object or None
            return_stmt = f"{wrapper_name}({access_path}) if {access_path}.ByteSize() > 0 else None"
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
        parent_wrapper = parent_name.replace('Proto', '')
        class_decl = f"class {name}({parent_wrapper}):"
    else:
        class_decl = f"class {name}:"
    
    # Module for proto type
    module_import = info['module'].split('.')[-1]  # e.g., 'resolved_ast_pb2'
    
    # Generate __init__
    # For nested types, use module.ParentProto.NestedProto format
    proto_type_hint = f"'{module_import}.{proto_full_path}'"
    
    init_lines = [
        f"    def __init__(self, proto: {proto_type_hint}):",
        f"        self._proto = proto"
    ]
    
    init_method = '\n'.join(init_lines)
    
    # Generate properties for ALL fields (own + inherited)
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
            
            prop = generate_property(field, chain)
            properties.append(prop)
    
    # Then generate own fields (no parent chain)
    for field in info['own_fields']:
        prop = generate_property(field, [])
        properties.append(prop)
    
    # Combine all parts
    parts = [
        class_decl,
        f'    """Generated wrapper for {proto_name}"""',
        '',
        init_method
    ]
    
    if properties:
        parts.append('')
        parts.extend(properties)
    
    return '\n'.join(parts)


def generate_wrapper_file(graph: Dict[str, Any], output_path: Path) -> None:
    """Generate complete wrapper Python file"""
    print(f"\nGenerating wrapper file: {output_path}")
    
    # Sort by depth (parents first)
    sorted_names = sorted(graph.keys(), key=lambda n: (graph[n]['depth'], n))
    
    # Collect all proto types by module for TYPE_CHECKING imports
    from collections import defaultdict
    proto_types_by_module = defaultdict(set)
    
    for name, info in graph.items():
        # Extract module path
        # Module is like: zetasql.wasi._pb2.zetasql.resolved_ast.resolved_ast_pb2
        module_name = info['module']
        proto_types_by_module[module_name].add(name)
    
    # Generate header
    lines = [
        '"""',
        'ZetaSQL ResolvedAST Python Wrappers',
        '',
        'Auto-generated wrapper classes for convenient proto field access.',
        'DO NOT EDIT MANUALLY - regenerate with scripts/generate_wrappers.py',
        '',
        'Usage:',
        '    from zetasql.resolved_ast_wrapper import ResolvedLiteral',
        '    ',
        '    proto = resolved_ast_pb2.ResolvedLiteralProto()',
        '    wrapper = ResolvedLiteral(proto)',
        '    ',
        '    # Convenient access with IDE autocompletion',
        '    print(wrapper.value)  # Instead of proto.value',
        '    print(wrapper.type)   # Instead of proto.parent.type',
        '"""',
        '',
        'from __future__ import annotations',
        'from functools import cached_property',
        'from typing import Optional, List, Any, TYPE_CHECKING',
        '',
        'if TYPE_CHECKING:',
    ]
    
    # Add proto module imports for TYPE_CHECKING
    # Create short alias for each module (e.g., parse_tree_pb2, resolved_ast_pb2)
    for module_path in sorted(proto_types_by_module.keys()):
        # Extract the last part as alias (e.g., 'resolved_ast_pb2' from 'zetasql.wasi._pb2.zetasql.resolved_ast.resolved_ast_pb2')
        module_alias = module_path.split('.')[-1]
        lines.append(f'    import {module_path} as {module_alias}')
    
    lines.extend(['', ''])
    
    # Generate classes
    class_count = 0
    for name in sorted_names:
        info = graph[name]
        class_code = generate_class(name, info, graph)
        lines.append(class_code)
        lines.append('\n')
        class_count += 1
    
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
        default=Path(__file__).parent.parent / 'src/zetasql/resolved_ast_wrapper.py',
        help='Output Python file'
    )
    
    args = parser.parse_args()
    
    if not args.base_dir.exists():
        print(f"Error: Base directory not found: {args.base_dir}")
        sys.exit(1)
    
    print("=" * 70)
    print("ZetaSQL Python Wrapper Generator")
    print("=" * 70)
    
    # Extract inheritance graph
    graph = extract_inheritance_graph(args.base_dir)
    
    # Generate wrapper file
    generate_wrapper_file(graph, args.output)
    
    print("\n" + "=" * 70)
    print("Generation complete!")
    print("=" * 70)
    print(f"\nGenerated file: {args.output}")
    print("\nYou can now use:")
    print("  from zetasql.resolved_ast_wrapper import ResolvedLiteral")


if __name__ == '__main__':
    main()
