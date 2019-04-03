"""
Problem:
Consider an array.
A second array is formed by shuffling the elements of the first array and deleting some random elements.
Given these two arrays, find which elements are missing in the second array.

Example: arr1 = [1, 2, 3, 5, 1, 7, 'a', 'b']
         arr2 = [1, 1, 7, 3, 2, 'b']
         --> Missing element is [5, 'a']
"""


def find_missing_elements(arr1, arr2):
    for element in arr2:
        if element in arr1:
            arr1.remove(element)
    return arr1


if __name__ == "__main__":
    arr1 = [1, 2, 3, 5, 1, 7, 'a', 'b']
    arr2 = [1, 1, 7, 3, 2, 'b']

    missing_elements = find_missing_elements(arr1, arr2)
    print('missing_elements are: ', missing_elements)
