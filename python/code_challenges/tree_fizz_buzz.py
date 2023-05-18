from data_structures.kary_tree import KaryTree, Node
import copy


def fizz_buzz_tree(tree):
    def fizz_buzz(node):
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)

        for child in node.children:
            fizz_buzz(child)

    if not tree.root:
        return None

    new_tree = copy.deepcopy(tree)
    fizz_buzz(new_tree.root)
    return new_tree
