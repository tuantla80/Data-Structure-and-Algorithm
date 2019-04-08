"""
Useful links
https://visualgo.net/en/sorting
https://www.toptal.com/developers/sorting-algorithms

Bubble sort:
O(n^2) = (n-1) + (n-2) + ...+ 1 = (n-1)*n /2

Note on swap (a, b)
- Common way:
    temp = a
    a = b
    b = temp
- Tricky way (just to know)
    a = a + b
    b = a - b  # a+b-b=a
    a = a - b  # a+b - a = b
- Python way
    a, b = b, a
"""


def bubble_sort(arr):
    for i in list(range(len(arr) - 1, 0, -1)):
        # n =len(arr) --> i = [n-1, n-2, n-3, 1]
        # since the max value is at the end of list, and so on
        for j in range(i):  # j run from 0 to i-1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    arr = [1, 2, 5, 0, 4]
    new_arr = bubble_sort(arr)
    print('after bubble sort', new_arr)
