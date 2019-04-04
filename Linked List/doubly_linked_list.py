class DoublyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None  # next node
        self.prevnode = None  # previous node


if __name__ == "__main__":
    a = DoublyLinkedList(value=1)
    b = DoublyLinkedList(value=2)
    c = DoublyLinkedList(value=3)

    # Make node b after node a
    a.nextnode = b  # make a linked list forward
    b.prevnode = a  # make a linked list backward

    # Make node c after node b
    b.nextnode = c  # make a linked list forward
    c.prevnode = b  # make a linked list backward

    # Accessing Forward (exactly the same as singly linked list
    print("\n Forward")
    print("Access to value of a node: ", a.value)
    print('Access to b node: ', a.nextnode)
    print("Access to value of b node: ", a.nextnode.value)
    print("Access to value of c node: ", a.nextnode.nextnode.value)

    # Accessing Backward
    print("\n Backward")
    print("Access to value of c node: ", c.value)
    print('Access to b node: ', c.prevnode)
    print("Access to value of b node: ", c.prevnode.value)
    print("Access to value of a node: ", c.prevnode.prevnode.value)

