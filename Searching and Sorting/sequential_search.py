"""
Sequential search for unordered and ordered list.
"""


def sequential_search_for_unordered_list(arr, element):
    for ele in arr:
        if ele == element:
            return True
    return False


def sequential_search_for_ordered_list(arr, element):
    for ele in arr:
        if ele == element:
            return True
        elif ele > element:
            return False  # Dont need to go over that value
    return False


if __name__ == "__main__":
    # Unordered list
    arr = [10, 9, 2, 3, 4, 5]
    element = 3
    print("is element={} found: {}".format(element, sequential_search_for_unordered_list(arr, element)))

    # Ordered list
    arr = [2, 3, 4, 5, 9, 10]
    element = 3
    print("is element={} found: {}".format(element, sequential_search_for_ordered_list(arr, element)))
