from data_structures.binary_tree import BinaryTree


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root


def breadth_first(tree):
    if tree.root is None:
        return []

    queue = [tree.root]
    traversal = []

    while len(queue) > 0:
        node = queue.pop(0)
        traversal.append(node.value)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return traversal
