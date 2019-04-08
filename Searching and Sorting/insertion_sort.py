"""
Useful links
https://visualgo.net/en/sorting
https://www.toptal.com/developers/sorting-algorithms

Insertion sort:
O(n^2) but better than O(n^2) of bubble and selection sorts
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]  # shift operation
            position -= 1
        # end of while
        arr[position] = current_value
    return arr


if __name__ == "__main__":
    arr = [1, 2, 5, 0, 4]
    new_arr = insertion_sort(arr)
    print('after insertion sort', new_arr)
