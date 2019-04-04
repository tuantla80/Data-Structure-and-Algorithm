"""
Problem:
Given a string in the form 'AAAbcddAA' compress to become 'A3b1c1d2A2'
Note: in this problem, even though 'b' in this case is only one, we still use 'b1'
"""


def string_compression(s):
    """
    Solution with O(n)
    """
    s_compress = ''
    count = 1  # count continuous occurrence of each letter

    # Check boundary
    length = len(s)
    if length == 0:
        return ''
    if length == 1:
        return s + str(1)

    previous_letter = s[0]
    for letter in s[1:]:
        if letter == previous_letter:
            count += 1
        else:
            s_compress += previous_letter + str(count)
            previous_letter = letter  # move the previous letter to the new one for the next run
            count = 1  # reset count for the next run
    # End of for
    # Calculate for the last letter
    s_compress += previous_letter + str(count)
    return s_compress


if __name__ == "__main__":
    s = 'AAAaaBCCCCdAAA'
    print("string is {} and its comression is {}".format(s, string_compression(s)))

    s = 'a'
    print("string is {} and its comression is {}".format(s, string_compression(s)))

