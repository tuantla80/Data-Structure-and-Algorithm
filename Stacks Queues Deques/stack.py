class Stack(object):
    """
    Using list to implement Stack
    Stack is LIFO (Last In First Out)
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        To check whether the stack is empty or not
        """
        return self.items == []

    def push(self, item):
        """
        To adds a new item to the top of the stack
        """
        self.items.append(item)

    def pop(self):
        """
        To remove the top item from the stack
        """
        return self.items.pop()

    def peek(self):
        """
        To return the top item from the stack but does not remove it
        """
        return self.items[len(self.items) - 1]

    @property
    def size(self):
        """
        To return the number of items on the stack
        """
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    print('is stack empty: {}'.format(stack.is_empty()))
    stack.push(10)
    stack.push('A')
    stack.push('B')
    print('stack is: {}'.format(stack.items))
    stack.pop()  # will remove 'B'
    print('stack is: {}'.format(stack.items))
    peek_item = stack.peek()
    print('peek_item = ', peek_item)
    print('size of stack = ', stack.size)
