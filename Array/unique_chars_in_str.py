"""
Problem:
Given a string, determine if it is comprised of all unique characters.
For example: The string 'abcdef' has all unique characters and should return True.
             The string 'abcdefa' contains duplicate characters and should return False.
"""

def uni_chars_in_str(s):
    """
    Solution using set() in Python
    """
    return len(set(s)) == len(s)


if __name__ == "__main__":
    s = 'abcdef'
    print('string is: {} \nIs it unique characters in string? {}'.format(s, uni_chars_in_str(s)))

    print('\n')
    s = 'abcdefa'
    print('string is: {} \nIs it unique characters in string? {}'.format(s, uni_chars_in_str(s)))
