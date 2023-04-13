from data_structures.linked_list import LinkedList, Node


def zip_lists(a, b):
    current1 = a.head
    current2 = b.head

    if a.head:
        new_ll = LinkedList(a.head)
        current1 = current1.next_
        current_new = new_ll.head

    else:
        return b

    while current1 and current2:
        current_new.next_ = Node(current2.value)
        current2 = current2.next_
        current_new = current_new.next_

        current_new.next_ = Node(current1.value)
        current1 = current1.next_
        current_new = current_new.next_

    while current1:
        current_new.next_ = Node(current1.value)
        current1 = current1.next_
        current_new = current_new.next_

    while current2:
        current_new.next_ = Node(current2.value)
        current2 = current2.next_
        current_new = current_new.next_

    return new_ll



