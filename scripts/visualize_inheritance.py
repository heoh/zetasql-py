"""Visualize the inheritance graph of generated wrappers"""
import sys
from pathlib import Path
from collections import defaultdict

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Import the generator to reuse the graph extraction logic
from generate_wrappers import extract_inheritance_graph


def visualize_graph(graph: dict, output_file: str = "inheritance_graph.txt", 
                    root_filter: str = None, max_depth: int = None):
    """Generate a text-based tree visualization of the inheritance graph"""
    
    # Find root nodes (no parent or parent not in graph)
    roots = [name for name, info in graph.items() 
             if not info['parent'] or info['parent'] not in graph]
    
    # Filter roots if specified
    if root_filter:
        roots = [r for r in roots if root_filter in r]
    
    lines = []
    lines.append("=" * 80)
    lines.append("ZetaSQL Inheritance Graph")
    lines.append("=" * 80)
    lines.append(f"\nTotal classes: {len(graph)}")
    lines.append(f"Root classes: {len(roots)}")
    lines.append("")
    
    def print_tree(name: str, prefix: str = "", is_last: bool = True, depth: int = 0):
        """Recursively print tree structure"""
        if max_depth is not None and depth > max_depth:
            return
        
        info = graph[name]
        connector = "└── " if is_last else "├── "
        
        # Class info
        own_field_count = len(info['own_fields'])
        all_field_count = len(info['all_fields'])
        inherited = all_field_count - own_field_count
        
        class_info = f"{name.replace('Proto', '')} [{own_field_count} own, {inherited} inherited]"
        lines.append(f"{prefix}{connector}{class_info}")
        
        # Update prefix for children
        extension = "    " if is_last else "│   "
        new_prefix = prefix + extension
        
        # Print children
        children = sorted(info['children'])
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            print_tree(child, new_prefix, is_last_child, depth + 1)
    
    # Print each root tree
    for i, root in enumerate(sorted(roots)):
        if i > 0:
            lines.append("")
        print_tree(root, "", True, 0)
    
    # Statistics
    lines.append("")
    lines.append("=" * 80)
    lines.append("Statistics")
    lines.append("=" * 80)
    
    # Depth distribution
    depth_counts = defaultdict(int)
    for info in graph.values():
        depth_counts[info['depth']] += 1
    
    lines.append("\nDepth distribution:")
    for depth in sorted(depth_counts.keys()):
        lines.append(f"  Depth {depth}: {depth_counts[depth]} classes")
    
    # Top classes by field count
    lines.append("\nTop 10 classes by total field count:")
    sorted_by_fields = sorted(graph.items(), 
                             key=lambda x: len(x[1]['all_fields']), 
                             reverse=True)
    for name, info in sorted_by_fields[:10]:
        lines.append(f"  {name.replace('Proto', '')}: {len(info['all_fields'])} fields "
                    f"({len(info['own_fields'])} own + {len(info['all_fields']) - len(info['own_fields'])} inherited)")
    
    # Top parent classes by children count
    lines.append("\nTop 10 parent classes by children count:")
    sorted_by_children = sorted(graph.items(), 
                               key=lambda x: len(x[1]['children']), 
                               reverse=True)
    for name, info in sorted_by_children[:10]:
        if info['children']:
            lines.append(f"  {name.replace('Proto', '')}: {len(info['children'])} direct children")
    
    # Write to file
    output_path = Path(__file__).parent.parent / output_file
    content = "\n".join(lines)
    output_path.write_text(content)
    print(f"\nInheritance graph saved to: {output_path}")
    print(f"Total lines: {len(lines)}")
    
    return content


def generate_graphviz(graph: dict, output_file: str = "inheritance_graph.dot",
                     root_filter: str = None, max_nodes: int = 100):
    """Generate a Graphviz DOT file for visualization"""
    
    lines = []
    lines.append("digraph InheritanceGraph {")
    lines.append("  rankdir=BT;")  # Bottom to top (child -> parent)
    lines.append("  node [shape=box, style=filled, fillcolor=lightblue];")
    lines.append("")
    
    # Filter nodes
    if root_filter:
        # Find all descendants of filtered roots
        roots = [name for name, info in graph.items() 
                if root_filter in name and (not info['parent'] or info['parent'] not in graph)]
        
        included = set()
        def add_descendants(name):
            if name not in graph:
                return
            included.add(name)
            for child in graph[name]['children']:
                add_descendants(child)
        
        for root in roots:
            add_descendants(root)
        
        filtered_graph = {k: v for k, v in graph.items() if k in included}
    else:
        # Just take top N by depth and field count
        sorted_nodes = sorted(graph.items(), 
                            key=lambda x: (x[1]['depth'], -len(x[1]['all_fields'])))
        filtered_graph = dict(sorted_nodes[:max_nodes])
    
    # Add nodes
    for name, info in filtered_graph.items():
        label = name.replace('Proto', '')
        own_fields = len(info['own_fields'])
        all_fields = len(info['all_fields'])
        
        # Color by depth
        colors = ['lightgreen', 'lightblue', 'lightyellow', 'lightpink', 'lightgray']
        color = colors[min(info['depth'], len(colors) - 1)]
        
        lines.append(f'  "{label}" [label="{label}\\n{own_fields}/{all_fields} fields", '
                    f'fillcolor={color}];')
    
    lines.append("")
    
    # Add edges
    for name, info in filtered_graph.items():
        if info['parent'] and info['parent'] in filtered_graph:
            child_label = name.replace('Proto', '')
            parent_label = info['parent'].replace('Proto', '')
            lines.append(f'  "{child_label}" -> "{parent_label}";')
    
    lines.append("}")
    
    # Write to file
    output_path = Path(__file__).parent.parent / output_file
    content = "\n".join(lines)
    output_path.write_text(content)
    print(f"Graphviz DOT file saved to: {output_path}")
    print(f"To generate PNG: dot -Tpng {output_file} -o inheritance_graph.png")
    print(f"Or view online: https://dreampuf.github.io/GraphvizOnline/")
    
    return content


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Visualize ZetaSQL wrapper inheritance graph')
    parser.add_argument('--base-dir', type=str,
                       default=str(Path(__file__).parent.parent / 'src' / 'zetasql' / 'wasi' / '_pb2'),
                       help='Base directory containing _pb2.py files')
    parser.add_argument('--filter', type=str, default='Resolved',
                       help='Filter to show only classes containing this string')
    parser.add_argument('--max-depth', type=int, default=None,
                       help='Maximum depth to show in text tree')
    parser.add_argument('--format', choices=['text', 'dot', 'both'], default='both',
                       help='Output format')
    parser.add_argument('--max-nodes', type=int, default=100,
                       help='Maximum nodes for graphviz output')
    
    args = parser.parse_args()
    
    print("Extracting inheritance graph...")
    graph = extract_inheritance_graph(Path(args.base_dir))
    
    if args.format in ['text', 'both']:
        print("\n" + "=" * 80)
        print("Generating text visualization...")
        print("=" * 80)
        visualize_graph(graph, 
                       output_file='inheritance_graph.txt',
                       root_filter=args.filter,
                       max_depth=args.max_depth)
    
    if args.format in ['dot', 'both']:
        print("\n" + "=" * 80)
        print("Generating Graphviz DOT file...")
        print("=" * 80)
        generate_graphviz(graph,
                         output_file='inheritance_graph.dot',
                         root_filter=args.filter,
                         max_nodes=args.max_nodes)
    
    print("\n" + "=" * 80)
    print("Done!")
    print("=" * 80)


if __name__ == '__main__':
    main()
