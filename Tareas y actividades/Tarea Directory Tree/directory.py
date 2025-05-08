import os
import sys
from tree import Tree, Node

def build_tree(path):
    root_name = os.path.basename(path) or path
    root = Tree(root_name)
    _scan_directory(path, root)
    return root

def _scan_directory(path, tree):
    try:
        entries = os.listdir(path)
    except PermissionError:
        return

    for entry in sorted(entries):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            subtree = Tree(entry)
            tree.insert_child(subtree)
            _scan_directory(full_path, subtree)
        else:
            node = Node(entry)
            tree.insert_child(node)

def print_tree(tree, indent=""):
    print(f"{indent}- {tree.name}/")
    for child in tree.get_children():
        if isinstance(child, Tree):
            print_tree(child, indent + "    ")
        else:
            print(f"{indent}    - {child.name}")

if __name__ == "__main__":
    path = input("Ingrese la ruta del directorio (PATH): ").strip()

    if not os.path.exists(path):
        print(f"El path '{path}' no existe o no ha sido encontrado.")
        sys.exit(1)

    directory_tree = build_tree(path)
    print("\nDirectory tree generado:")
    print_tree(directory_tree)
