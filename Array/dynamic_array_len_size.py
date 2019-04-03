"""
This example is to see how to assign bytes dynamically to a list in Python
Output: (note the increase in chunk size)
    len=0, size in bytes=64
    len=1, size in bytes=96
    len=2, size in bytes=96
    len=3, size in bytes=96
    len=4, size in bytes=96
    len=5, size in bytes=128
    len=6, size in bytes=128
    len=7, size in bytes=128
    len=8, size in bytes=128
"""
import sys

n = 9
data = []

for i in range(n):
    num_elements = len(data)
    actual_size_in_bytes = sys.getsizeof(data)
    print('len={}, size in bytes={}'.format(num_elements, actual_size_in_bytes))
    data.append(n)
