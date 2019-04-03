"""
Problem:
Given an integer array, output all the unique pairs that sum up to a specific value k.
So the input:
    pair_sum([1, 5, 6, 3, 2, 7, 7], 8)
    would return 2 pairs:
         (1, 7), (5,3), (6, 2)
"""


def array_unique_pair_sum(arr, k):
    lookup = set()
    output = set()
    for number in arr:
        if (k - number) in lookup:
            output.add((k - number, number))
        else:
            lookup.add(number)
    return output


if __name__ == "__main__":
    arr = [1, 5, 6, 3, 2, 7, 7]
    k = 8
    output = array_unique_pair_sum(arr, k)
    print(" number of pairs = {} \n output = \n {}".format(len(output), '\n '.join(map(str, output))))

