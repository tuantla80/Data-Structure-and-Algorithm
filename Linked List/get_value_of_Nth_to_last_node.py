"""
This code is to take a head node and an integer value n and
then returns the nth to last node in the linked list.
For example:
    a = SinglyLinkedList(value=1)
    b = SinglyLinkedList(value=2)
    c = SinglyLinkedList(value=3)
    d = SinglyLinkedList(value=4)

    a.nextnode = b  # make a linked list
    b.nextnode = c  # make a linked list
    c.nextnode = d  # make a linked list

    v = get_value_of_Nth_to_last_node(head=a, n=2)
    Output:  v = 3
"""

class SinglyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def get_value_of_Nth_to_last_node_simple_solution(head, n):

    # Count number of nodes in the linked list
    currentNode = head
    count_node = 0
    while currentNode:
        count_node += 1
        currentNode = currentNode.nextnode

    # Check boundary
    if n > count_node:
        raise LookupError("Error: n is larger than number of nodes")

    # Find which node is the nth to last node in the linked list
    currentNode = head
    i = 0
    while currentNode:
        i += 1
        if i == count_node - n + 1:
            return currentNode
        # End of if
        currentNode = currentNode.nextnode


def get_value_of_Nth_to_last_node(head, n):
    """
    Let's imagine, we have a bunch of nodes and a "block" that contain n-nodes.
    We can walk this "block" all the way down the list and once the front of the block reached the end,
    the the other end of the block would be the Nth node.
    """
    left_pointer = right_pointer = head

    # Moving the right_pointer to a right position of the "block" mentioned above
    for i in range(n-1):
        # Check boundary
        if not right_pointer.nextnode:
            raise LookupError("Error: n is larger than number of nodes")
        right_pointer = right_pointer.nextnode
    # End of for

    # Moving left_pointer and right_pointer in a synchronization way
    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer


if __name__ == "__main__":

    a = SinglyLinkedList(value=1)
    b = SinglyLinkedList(value=2)
    c = SinglyLinkedList(value=3)
    d = SinglyLinkedList(value=4)

    a.nextnode = b  # make a linked list
    b.nextnode = c  # make a linked list
    c.nextnode = d  # make a linked list

    chosen_node = get_value_of_Nth_to_last_node_simple_solution(head=a, n=2)
    print("At simple solution, value = ", chosen_node.value)

    chosen_node = get_value_of_Nth_to_last_node(head=a, n=2)
    print('At "block" solution, value =', chosen_node.value)



