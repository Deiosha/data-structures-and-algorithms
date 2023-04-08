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
        pass

    def insert(self, value):
        old_head = self.head
        self.head = Node(value)
        self.head.next = old_head

    def __str__(self):
        current_value = self.head
        ll_list = []
        while current_value is not None:
            ll_list.append(str(current_value.value))
            current_value = current_value.next
        return " -> ".join(["{ " + value + " }" for value in ll_list] + ["NULL"])

    def includes(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, new_value):

        current = self.head
        new_node = Node(new_value)

        if current is None:
            self.head = new_node
            return

        while current.next:
            current = current.next

        current.next = new_node

    def insert_before(self, target_value, new_value):
        if self.head is None:
            raise TargetError("invalid value: " + target_value)

        if self.head.value == target_value:
            self.insert(new_value)
            return

        current = self.head
        while current.next is not None:
            if current.next.value == target_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        raise TargetError("invalid value: " + target_value)

    def insert_after(self, target_value, new_value):
        if self.head is None:
            raise TargetError(target_value + " nonexistent")

        current = self.head
        while current is not None:
            if current.value == target_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        raise TargetError(target_value + " nonexistent")


class TargetError(Exception):
    pass

