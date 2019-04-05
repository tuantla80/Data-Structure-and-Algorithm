"""
This code is to reverse a Linked List in place
"""

class SinglyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reversal(head):

    prevNode = None
    currentNode = head  # head of the linked list
    # nextNode = None

    while currentNode:
        nextNode = currentNode.nextnode  # get the next_note of current linked list structure
        currentNode.nextnode = prevNode  # set current_note to the new linked list structure (reversal)

        prevNode = currentNode  # move prevNode to the next one
        currentNode = nextNode  # move prevNode to the next one


if __name__ == "__main__":

    a = SinglyLinkedList(value=1)
    b = SinglyLinkedList(value=2)
    c = SinglyLinkedList(value=3)
    d = SinglyLinkedList(value=4)

    a.nextnode = b  # make a linked list
    b.nextnode = c  # make a linked list
    c.nextnode = d  # make a linked list

    print('The linked list:\n a.nextnode.value = {} \n b.nextnode.value = {} \n c.nextnode.value {}'.
          format(a.nextnode.value, b.nextnode.value, c.nextnode.value))

    reversal(a)

    print('\nThe linked list after reversal:\n d.nextnode.value = {} \n c.nextnode.value = {} \n b.nextnode.value {}'.
          format(d.nextnode.value, c.nextnode.value, b.nextnode.value))



