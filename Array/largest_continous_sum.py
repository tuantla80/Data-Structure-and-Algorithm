"""
Problem:
Given an array of positive and/or negative integers, find the largest continuous sum.
Ex.
"""


def largest_continuous_sum(arr):
    if len(arr) == 0:
        raise 'arr is empty'

    current_sum = max_sum = arr[0]
    print("number={}, current_sum={}, max_sum={}".format(arr[0], current_sum, max_sum))

    for number in arr[1:]:
        current_sum = max(current_sum + number, number)
        max_sum = max(max_sum, current_sum)
        print("number={}, current_sum={}, max_sum={}".format(number, current_sum, max_sum))
    return max_sum


if __name__ == "__main__":
    max_sum = largest_continuous_sum([4, -2, 3, 9, 9 , -10, -1])
    print(max_sum)
