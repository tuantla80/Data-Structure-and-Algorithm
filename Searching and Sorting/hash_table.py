"""
hash table: a data structure
            2 main components (key: value)
hash function: def hash(key) --> to get index
- load_factor = number_of_items/table_size (in Python, implement hast table as a list so table_size is a list_size)
- if load_factor < 1, we can simply use perfect hash function with index = item % tabel_size
  if item is not integer, we can change it to number by using ordinal function. In Python using ord() to change to ASCII
   Ex. table_size=11
        cat = ord ('c') + ord('a') + ord('t') = 99 + 97 + 116 =312.
        312%11=4  --> cat will store in a slot of a list with index=4
- Collision:
  One way to avoid it is a chaining method.
  Those items, having the same index, will store in a linked list that is placed at this index.

NOTE: Python already has a built-in dictionary object that serves as a Hash Table
Ref: https://www.youtube.com/watch?v=KyUTuwz_b7Q
    https://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented
"""

class HashTable(object):

    def __init__(self, size):
        # size is len of array
        self.slots = [None] * size  # a list to store key (to be changed to index)
        self.data = [None] * size   # a list to store data corresponding to key


    def hash_func(self, key, size):
        """
        Using Remainder Method
        key is integer number of item after using ord() function
        size is len of array (slots)

        return: hash_value which is an index of array corresponding to key and size
        """
        hash_value = key % size
        return hash_value


    def rehash(self, old_hash_value, size):

        new_hash_value = (old_hash_value + 1) % size  # moving a long arr and try to find an empty slot
        return new_hash_value


    def put(self, key, _data):
        """
        Usually we need to get key as integer number, but in here we assume it as an integer for simplicity.
        """
        # Get the hash value
        hash_value = self.hash_func(key, len(self.slots))

        if self.slots[hash_value] == None:  # slot is Empty, put key and data
            self.slots[hash_value] = key
            self.data[hash_value] = _data
        else:
            if self.slots[hash_value] == key: # key already exists, replace old value
                self.data[hash_value] = _data
            else:  # otherwise, rehash (find the next available slot)
                next_slot = self.rehash(hash_value, len(self.slots))
                # Get to the next slot
                while self.slots[next_slot] != None and self.slots[next_slot] != key: # next_slot alread existed, find new one
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:  # Set new key, if none
                    self.slots[next_slot] = key
                    self.data[next_slot] = _data
                else:  # Otherwise replace old value
                    self.data[next_slot] = _data


    def get(self, key):
        """
        To items given a key
        """
        hash_value = self.hash_func(key, len(self.slots))
        while self.slots[hash_value] != None:
            if self.slots[hash_value] == key:
                return self.data[hash_value]
            else:
                hash_value = self.rehash(hash_value, len(self.slots))
        return False

    # special methods for use with Python indexing
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, _data):
        self.put(key, _data)

if __name__ == "__main__":
    hash_table = HashTable(size=5)
    hash_table[1] = 'abc'
    hash_table.put(key=2, _data=10)
    hash_table.put(key=3, _data=20)

    print(" hash_table[1] = ",  hash_table[1])  # return abc
    print(" get = ", hash_table.get(key=1))  # return abc
    print(" get = ", hash_table.get(key=10)) # return None