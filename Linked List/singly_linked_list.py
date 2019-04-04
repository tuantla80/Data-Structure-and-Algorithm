class SinglyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


if __name__ == "__main__":
    a = SinglyLinkedList(value=1)
    b = SinglyLinkedList(value=2)
    c = SinglyLinkedList(value=3)

    a.nextnode = b  # make a linked list
    b.nextnode = c  # make a linked list

    print("Access to value of a node: ", a.value)
    print('Access to b node: ', a.nextnode)
    print("Access to value of b node: ", a.nextnode.value)
    print("Access to value of c node: ", a.nextnode.nextnode.value)

