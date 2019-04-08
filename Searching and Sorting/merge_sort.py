"""
Useful links
https://visualgo.net/en/sorting
https://www.toptal.com/developers/sorting-algorithms

Merger sort: recursive algorithm that continually splits a list in a haft,......
O(nlogn)

Ref: https://en.wikipedia.org/wiki/Merge_sort
"""


def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # recursive
    middle = len(arr) // 2
    left, right = merge_sort(arr[: middle]), merge_sort(arr[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    # Either the element in the left array or the right array
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result


if __name__ == "__main__":
    arr = [1, 2, 5, 0, 4]
    arr = [1, 2, 4, 2, 10, 12, 1222, 145, 2]
    sorted_arr = merge_sort(arr)
    print('after merge sort: ', sorted_arr)
