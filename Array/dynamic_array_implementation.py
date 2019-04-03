"""
This code is to implement a dynamic array (similar to Python list)
Note: class in Python: public vs private methods.
      Using an underscore _ before the method name to keep it non-public
Ref: https://docs.python.org/3/library/ctypes.html
"""
import ctypes
import sys


class DynamicArray(object):

    def __init__(self, n=0, capacity=1):
        self.n = n  # number of elements (default n=0, means A=[])
        self.capacity = capacity  # Default capacity is 1 element (capacity=1)
        self.A = self.make_array(self.capacity)  # A is an array

    def __len__(self):
        """
        Get number of elements sorted in an array
        Usage: len(_array)
        """
        return self.n

    def __getitem__(self, k):
        """
        Get an element of the array at index k
        Usage: _array[k]
        """
        if not 0 <= k < self.n:
            return IndexError('k is out of bounds!')

        return self.A[k]  # get element at index k

    def append(self, element):
        """
        Add an element to end of the array
        """
        if self.n == self.capacity:
            self._resize(2 * self.capacity)  # Make a 2x if not enough capacity

        self.A[self.n] = element  # Set self.n index to element
        self.n += 1

    def _resize(self, new_capacity):
        """
        Resize capacity of internal array to new_capacity
        """
        B = self.make_array(new_capacity)  # make a new bigger array

        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]

        self.A = B  # A is now a new bigger array
        self.capacity = new_capacity  # reset the capacity

    def make_array(self, new_capacity):
        """
        Returns a new array with new_capacity
        """
        return (new_capacity * ctypes.py_object)()


def test_DynamicArray():
    _array = DynamicArray()
    _array.append("test1")
    _array.append("test2")
    print("len = {}, _array[0]={}, _array[1]={}".format(len(_array), _array[0], _array[1]))


if __name__ == "__main__":
    test_DynamicArray()
