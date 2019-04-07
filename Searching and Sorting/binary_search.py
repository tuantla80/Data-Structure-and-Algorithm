"""
Binary search of ordered list:
    - Start by examining the middle item
    - Devide and conquer
"""


def binary_search(arr, element):
    first_index, last_index = 0, len(arr) - 1

    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2  # ex. 7//2=3
        if arr[middle_index] == element:
            return True
        elif arr[middle_index] < element:
            first_index = middle_index + 1
        else:  # arr[middle_index] > element:
            last_index = middle_index - 1
    # End of while
    return False


def binary_search_using_recursive(arr, element):

    # Base case
    if len(arr) == 0:
        return False

    middle_index = len(arr) // 2
    if arr[middle_index] == element:
        return True
    elif arr[middle_index] < element:
        return binary_search_using_recursive(arr[middle_index + 1: ], element)
    else:  # arr[middle_index] > element:
        return binary_search_using_recursive(arr[: middle_index], element)


if __name__=="__main__":

    arr = [2, 3, 4, 5, 9, 10] # Unordered list
    element = 4
    print("is element={} found: {}".format(element, binary_search(arr, element)))

    arr = [2, 3, 4, 5, 9, 10]  # Unordered list
    element = 4
    print("is element={} found: {}".format(element, binary_search_using_recursive(arr, element)))