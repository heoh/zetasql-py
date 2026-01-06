import inspect
import sys
from collections import defaultdict

sys.path.insert(0, "src")

from zetasql.types import proto_model as pm_module
from zetasql.types.proto_model.proto_model import ProtoModel

with open("proto_model_hierarchy.txt", "w") as output_file:
    sys.stdout = output_file

    # Get all ProtoModel subclasses
    classes = {}
    for name in dir(pm_module):
        obj = getattr(pm_module, name)
        if inspect.isclass(obj) and issubclass(obj, ProtoModel) and obj != ProtoModel:
            classes[name] = obj

    # Build parent-child relationships
    children = defaultdict(list)
    for name, cls in classes.items():
        bases = [b.__name__ for b in cls.__bases__ if b != ProtoModel and issubclass(b, ProtoModel)]
        if not bases:
            children["ProtoModel"].append(name)
        else:
            for base in bases:
                children[base].append(name)

    # Sort children
    for parent in children:
        children[parent].sort()

    def print_tree(node, prefix="", is_last=True, visited=None):
        if visited is None:
            visited = set()

        if node in visited and node != "ProtoModel":
            return
        visited.add(node)

        # Print current node
        if node != "ProtoModel":
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{node}")
            prefix += "    " if is_last else "│   "

        # Print children
        child_list = children.get(node, [])
        for i, child in enumerate(child_list):
            is_last_child = i == len(child_list) - 1
            print_tree(child, prefix, is_last_child, visited)

    # Print the tree starting from ProtoModel
    print("ProtoModel")
    print_tree("ProtoModel", "", True)
