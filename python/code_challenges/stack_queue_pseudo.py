from data_structures.stack import Stack


class PseudoQueue:

    # first step is to create __init__ that takes in self
    def __init__(self):
        # creating empty list
        self.stack1 = []
        # creating empty list
        self.stack2 = []

    # adding a new element which is value
    def enqueue(self, value):
        # append is used to add the new value to the stack
        self.stack1.append(value)

    # used to remove the oldest element. This will be found in stack2
    def dequeue(self):
        # if the length in stack 1 is equal to 0 then return none (ensuring its empty)
        if len(self.stack1) == 0:
            return None

        # Now I am saying while the length in stack1 is greater than 0 will run until empty
        while len(self.stack1) > 0:
            # removing the top value in stack1 with pop then adds to stack2 using append
            self.stack2.append(self.stack1.pop())

        # removing the value in stack2 with pop
        value = self.stack2.pop()
        # Now I am saying while the length in stack2 is greater than 0 will run until empty
        while len(self.stack2) > 0:
            #  removes the oldest element from stack2 using the pop(),
            #  adds the removed element to the top of stack1 using append
            #  adds the element to the end of stack1
            self.stack1.append(self.stack2.pop())

        # returning the value
        return value

    if __name__ == "__main__":
        pass
