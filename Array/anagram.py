"""
This code is to solve the below problem

Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
    Input: s1 = "Anagram", s2 = "na  ga  ram"
    Output: true

Example 2:
    Input: s1 = "rat", s2 = "car"
    Output: false
"""


def anagram_simple_solution(s1, s2):
    """
    Method 1:
    It is a simple code but about O(n*log(n))
    """
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    for letter in s1:
        if letter in s2:
            s2 = s2.replace(letter, '', 1)  # note: replace only 1 character
        else:
            return False
    return True


def anagram(s1, s2):
    """
    Method 2:
    It is an efficient code with O(n)
    """
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    counter = {}

    # Count number of each letter in s1
    for letter in s1:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    print(counter)

    # Check each letter in s2 and reduce the counter to compare with s1
    for letter in s2:
        if letter in counter:
            counter[letter] -= 1
        else:
            return False

    # Check the final result in counter
    for k in counter.keys():
        if counter[k] !=0:
            return False

    return True


def test(s1, s2, sol):
    print('s1 is anagram of s2: {}'.format(sol(s1, s2)))


if __name__ == "__main__":
    test(s1="Anagram", s2="na  ga  ram", sol=anagram_simple_solution)
    test(s1="rat", s2="car", sol=anagram_simple_solution)

    test(s1="Anagram", s2="na  ga  ram", sol=anagram)
    test(s1="rat", s2="car", sol=anagram)
