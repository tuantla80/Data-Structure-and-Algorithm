class CreatQueueFrom2Stack:
    """
    Using 2 stacks (in this code stack is a Python list) to create a queue (also a Python list)
    Stack: LIFO ((Last In First Out)
    Queue: FIFO (First In First Out)
    """

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # End of if
        return self.out_stack.pop()


if __name__ == "__main__":

    queue = CreatQueueFrom2Stack()
    for i in range(10):
        queue.enqueue(i)
    print(queue.in_stack)  # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    item = queue.dequeue()
    print('item = ', item)  # output: item = 0 so it is a queue (First In First Out)
