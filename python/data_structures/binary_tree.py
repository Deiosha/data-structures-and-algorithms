class BinaryTree:
    """
    implementing a binary tree.
    """

    def __init__(self):
        # initialization here
        pass

    def pre_order(self):
        values = []

        def traversing(root):
            # Add value to list. 

            if root == None:
                return
                # return if nothing in the node
            values.append(root.value)

            # left
            if root.left:
                traversing(root.left)

            # right
            if root.right:
                traversing(root.right)

        traversing(self.root)

        return values

    def in_order(self):
        # Left, root, right

        values = []

        def traversing(root):
            # Add value to list.
            if root == None:
                return
                # return if there is nothing in the node
            # go left
            if root.left:
                traversing(root.left)

            values.append(root.value)

            # go right
            if root.right:
                traversing(root.right)

        traversing(self.root)

        return values

    def post_order(self):
        # Left, right, root

        values = []

        def traversing(root):
            # Add value to list.

            if root == None:
                return

            if root.left:
                traversing(root.left)

            if root.right:
                traversing(root.right)

            values.append(root.value)

        traversing(self.root)

        return values


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
