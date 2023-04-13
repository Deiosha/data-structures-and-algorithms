class LinkedList:
    """
    Pass in a head node to implement a linked list.
    """

    def __init__(self, head=None):
        # initialization here
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next_ = self.head
        self.head = node

    def __str__(self):
        current = self.head
        printout = ''
        while current is not None:
            printout += f'{{ {current.value} }} -> '
            current = current.next_
        printout += f'NULL'
        return printout

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value is value:
                return True
            current = current.next_
        return False

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next_:
                current = current.next_
            current.next_ = node

    def insert_before(self, value, new_value):
        if self.head is None:
            raise TargetError('Empty list')

        if not self.includes(value):
            raise TargetError('Value not found')

        if self.head.value is value:
            node = Node(new_value, self.head)
            self.head = node
        else:
            current = self.head
            while current:
                if current.next_.value is value:
                    node = Node(new_value, current.next_)
                    current.next_ = node
                    break
                else:
                    current = current.next_

    def insert_after(self, value, new_value):
        if self.head is None:
            raise TargetError('Empty list')

        if not self.includes(value):
            raise TargetError('Value not found')

        current = self.head
        while current:
            if current.value is value:
                node = Node(new_value, current.next_)
                current.next_ = node
                break
            else:
                current = current.next_

    def kth_from_end(self, k):
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next_

        target = length - k

        if k >= length:
            raise TargetError('k exceeds list length')

        if k < 0:
            raise TargetError('k must be a positive integer')

        if target == 0:
            return self.head.value

        current = self.head

        for i in range(target - 1):
            current = current.next_

        return current.value

    def reverse(self):
        if not self.head:
            return None

        prev = None
        curr = self.head

        while curr:
            next_node = curr.next_
            curr.next_ = prev
            prev = curr
            curr = next_node

        self.head = prev

    def add_one(self):
        self.reverse()
        curr = self.head

        while curr:
            if curr.value == 9 and curr.next_:
                curr.value = 0
                curr = curr.next_

            elif curr.value < 9:
                curr.value += 1
                break

            else:
                curr.value = 0
                curr.next_ = Node(1)
                break
        self.reverse()


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_


class TargetError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
