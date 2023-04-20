from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.items = []

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError()
        else:
            removed_node = self.front
            self.front = removed_node.next
            if self.front is None:
                self.rear = None
            return removed_node.value

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise InvalidOperationError


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class InvalidOperationError(Exception):
    pass
