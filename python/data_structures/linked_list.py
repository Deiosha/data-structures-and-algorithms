import self as self


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
        return " -> ".join(["{ " + value + " }" for value in new_val] + ["NULL"])

    def append(self, value):
        if self.head == None:
            self.head = Node(value, None)
        else:
            last_node = self.head
            while True:
                if last_node.next == None:
                    break
                last_node = last_node.next
            last_node.next = Node(value, None)

    def insert_before(self, value, new_value):

        node = Node(new_value)

        if not self.head:
            self.head = node
        else:
            current = self.head

        while current.next:
            if current.next.value == value:
                node.next = current.next
                current.next = node
                break
            else:
                current = current.next

    def insert_after(self, existing_value, new_value):
        new_node = Node(new_value, next)
        current = self.head

        if current == None:
            return 'Not here'

        while current:
            if current.value == existing_value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        return 'nope'




class TargetError:
    pass

