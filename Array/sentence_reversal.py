"""
Problem:
Given a string of words, reverse all the words.

Example: Given: 'This is a nice place  '
         Return: 'place nice a is This'
"""


def sentence_reversal(s):
    """
    Solution:
    - Step 1: split string into a list of words
    - Step 2: reverse the list
    - Step 3: join all the words to be a sentence
    Ref: split() refer to https://www.w3schools.com/python/ref_string_split.asp
    """
    return ' '.join(reversed(s.split()))


if __name__ == "__main__":
    print("reversed sentence: ", sentence_reversal(s='This is   a nice place  '))
