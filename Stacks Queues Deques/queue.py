class Queue:
    """
    Using list to implement Queue
    Queue is FIFO (First In First Out)
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        To check whether the queue is empty or not
        """
        return self.items == []

    def enqueue(self, item):
        """
        To adds a new item to the back (rear) of the queue
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        To remove the front item from the queue
        """
        return self.items.pop()

    @property
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()
    print('is queue empty: {}'.format(queue.is_empty()))
    queue.enqueue(10)
    queue.enqueue('A')
    queue.enqueue('B')
    print('queue is: {}'.format(queue.items))
    queue.dequeue()  # will remove 10
    print('queue is: {}'.format(queue.items))
    print('size of queue = ', queue.size)
