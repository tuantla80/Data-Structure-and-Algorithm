class SinglyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

def cycle_check(node):
    """
    To check of the singly linked list is cycle or not
    """
    node_marker1 = node_marker2 = node

    while node_marker2 and node_marker2.nextnode:
        node_marker1 = node_marker1.nextnode  # node_marker1 runs 1 node at each step
        node_marker2 = node_marker2.nextnode.nextnode   # node_marker2 runs 2 node at each step
        if node_marker1 == node_marker2:
            return True  # meaning that they are meeting each other at some point because of linked list is cycle.
    # End of while
    return False


if __name__ == "__main__":

    # TEST 1: Not a cycle
    a = SinglyLinkedList(value=1)
    b = SinglyLinkedList(value=2)
    c = SinglyLinkedList(value=3)
    a.nextnode = b  # make a linked list
    b.nextnode = c  # make a linked list
    print("is the linked list (a b c) cycle? : {}".format(cycle_check(node=a)))
    print("\n")

    # TEST 2: a cycle
    x = SinglyLinkedList(value=1)
    y = SinglyLinkedList(value=2)
    z = SinglyLinkedList(value=3)
    x.nextnode = y
    y.nextnode = z
    z.nextnode = x   # It is Cycle
    print("is the linked list (x, y, z) cycle? : {}".format(cycle_check(node=x)))
    print("\n")


