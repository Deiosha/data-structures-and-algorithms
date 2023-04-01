class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        old_head = self.head
        self.head = Node(value)
        self.head.next = old_head

    def __str__(self):
        if self.head is None:
            return "NULL"

    def __str__(self):
        present = self.head
        new_val = []
        while present is not None:
            new_val.append(str(present.value))
            present = present.next
        return " -> ".join(["{ "+value+" }" for value in new_val] + ["NULL"])

    def includes(self, value):
        present = self.head
        new_val = []

        while present is not None:
            new_val.append(str(present.value))

        if value in present:
            return True
        else:
            return False





class TargetError:
    pass
