"""
Useful links
https://visualgo.net/en/sorting
https://www.toptal.com/developers/sorting-algorithms

Quick sort: recursive algorithm
Best: O(nlogn). Average: O(nlogn). Worst: O(n^2)
Ref: for visualization of quick sort https://www.youtube.com/watch?v=CB_NCoxzQnk
"""


def quick_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    smaller, equal, larger = [], [], []
    pivot_value = arr[0]  # choose pivot_value of first or last or
                          # a random value in arr or median value of several number
    for value in arr:
        if value < pivot_value:
            smaller.append(value)
        elif value == pivot_value:
            equal.append(value)
        else:
            larger.append(value)
    return quick_sort(smaller) + equal + quick_sort(larger) # sum here is to concatenate lists to single one


if __name__ == "__main__":
    #arr = [1, 2, 5, 0, 4]
    arr = [1, 2, 4, 2, 10, 12, 1222, 145, 2]
    sorted_arr = quick_sort(arr)
    print('after quick sort: ', sorted_arr)
