class Deque:
    """
    Using list to implement Deque
    Deque /deck/ is double-ended queue.
    We can add and remove items both at the front or at the back (rear)
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        To check whether the deque is empty or not
        """
        return self.items == []

    def add_at_front(self, item):
        """
        To adds a new item at the front of the deque
        """
        self.items.append(item)

    def add_at_back(self, item):
        """
        To adds a new item to the back (rear) of the deque
        """
        self.items.insert(0, item)

    def remove_at_front(self):
        """
        To remove the front item from the deque
        """
        return self.items.pop()

    def remove_at_back(self):
        """
        To remove the back (rear) item from the deque
        """
        return self.items.pop(0)

    @property
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    deque = Deque()
    print('is deque empty: {}'.format(deque.is_empty()))

    deque.add_at_front(10)
    deque.add_at_front("At Front")
    deque.add_at_back("At back")
    print('deque is: {}'.format(deque.items))

    deque.remove_at_front()  # remove "At Front"
    print('deque after remove at front is: {}'.format(deque.items))

    deque.remove_at_back()  # remove "Back"
    print('deque after remove at back is: {}'.format(deque.items))

    print('size of deque = ', deque.size)
