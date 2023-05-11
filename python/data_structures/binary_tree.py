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

    def find_maximum_value(self):
        """
        Returns the maximum value in the binary tree.
        """
        if not self.root:
            # returning None is no value is found
            return None

        def traverse(node):
            # Base case
            if not node:
                return float()

            # Recursive case
            # reading if the max equals to node value
            max_value = node.value
            #  move down the left and right sides of the tree
            left_max = traverse(node.left)
            right_max = traverse(node.right)

            # if the left max is more the max value
            if left_max > max_value:
                # max_value variable is updated to the new maximum value
                max_value = left_max
            # if the right max is more the max value
            if right_max > max_value:
                # max_value variable is updated to the new maximum value
                max_value = right_max
            # return the max value
            return max_value
        # function will traverse through binary tree, find the max value returned
        return traverse(self.root)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
