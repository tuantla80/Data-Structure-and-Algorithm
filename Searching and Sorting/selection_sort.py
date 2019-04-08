"""
Useful links
https://visualgo.net/en/sorting
https://www.toptal.com/developers/sorting-algorithms

Selection sort is an improvement of bubble sort by making only 1 exchange for every pass through the list
(For example, just exchange the selected value with max_value in the list)
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


def selection_sort(arr):
    for i in list(range(len(arr) - 1, 0, -1)):
        # n =len(arr) --> i = [n-1, n-2, n-3, 1]
        # since the max value is at the end of list, and so on
        max_index = 0
        for j in range(1, i + 1):  # j run from 0 to i-1
            if arr[j] > arr[max_index]:
                max_index = j
        # End of for
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr


if __name__ == "__main__":
    arr = [1, 2, 5, 0, 4]
    new_arr = selection_sort(arr)
    print('after selection sort', new_arr)
