"""
Problem:
Given a string, write a function that uses recursion to reverse it.
"""

def reverse_str(str):

    # based case
    if len(str) <= 1:
        return str

    # recursive
    return reverse_str(str[1: ]) + str[0]


if __name__ == "__main__":
    str = 'ADB 1h'
    str_reversed = reverse_str(str)
    print("str_reversed = ", str_reversed)