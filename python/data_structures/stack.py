class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            popped_node = self.top
            self.top = popped_node.next
            return popped_node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

    # def peek_empty(self):
    #     if self.top is None:
    #         raise InvalidOperationError("Method not allowed on empty collection")
    #     return self.top.value
    #
    # def pop_empty(self):
    #     if self.top is None:
    #         raise InvalidOperationError("Method not allowed on empty collection")
    #     value = self.top.value
    #     self.top = self.top.next
    #     return value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class InvalidOperationError(Exception):
    pass
