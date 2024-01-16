from graphviz import Digraph
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_balanced_binary_tree(ids):
    if not ids:
        return None

    sorted_ids = sorted(ids, reverse=True)
    return construct_tree(sorted_ids)

def construct_tree(sorted_ids):
    if not sorted_ids:
        return None

    mid = len(sorted_ids) // 2
    root = Node(sorted_ids[mid])

    root.left = construct_tree(sorted_ids[:mid])
    root.right = construct_tree(sorted_ids[mid + 1:])

    return root

def generate_dot_representation(root, parent_name, dot):
    current_name = f'"{root.value}"'
    dot.node(current_name)

    if parent_name is not None:
        dot.edge(parent_name, current_name)

    if root.left is not None:
        generate_dot_representation(root.left, current_name, dot)

    if root.right is not None:
        generate_dot_representation(root.right, current_name, dot)

# Example IDs
ids = ["I4", "S6", "S5", "S8", "S9", "I1", "S1", "I7", "A1", "A3", "S4", "I2", "S7", "I3", "S3", "A4", "I9", "I11", "A2", "S10", "S2", "S11", "I5", "I8", "I6", "I10"]

# Build the balanced binary tree
root = build_balanced_binary_tree(ids)

# Create a Digraph object
dot = Digraph(comment='Binary Tree')
generate_dot_representation(root, None, dot)

# Print the DOT representation
print(dot)
