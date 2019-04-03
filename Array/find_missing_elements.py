"""
Problem:
Consider an array.
A second array is formed by shuffling the elements of the first array and deleting some random elements.
Given these two arrays, find which elements are missing in the second array.

Example: arr1 = [1, 2, 3, 5, 1, 7, 'a', 'b']
         arr2 = [1, 1, 7, 3, 2, 'b']
         --> Missing element is [5, 'a']
"""


def find_missing_elements_simple_solution(arr1, arr2):
    """
    Solution with O(n^2)
    """
    for element in arr2:
        if element in arr1:
            arr1.remove(element)
    return arr1


def find_missing_elements(arr1, arr2):
    """
    Solution with O(n)
    Ref: https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
    """
    import collections
    d = collections.defaultdict(int)

    for element in arr2:
        d[element] += 1

    missing_elements = []
    for element in arr1:
        if d[element] == 0:
            missing_elements.append(element)
        else:
            d[element] -= 1
    return missing_elements


if __name__ == "__main__":
    missing_elements = find_missing_elements_simple_solution(arr1=[1, 2, 3, 5, 1, 7, 'a', 'b'],
                                                             arr2=[1, 7, 3, 2, 'b'])
    print('missing_elements are: ', missing_elements)

    missing_elements = find_missing_elements(arr1=[1, 2, 3, 5, 1, 7, 'a', 'b'],
                                             arr2=[1, 7, 3, 2, 'b'])
    print('missing_elements are: ', missing_elements)
