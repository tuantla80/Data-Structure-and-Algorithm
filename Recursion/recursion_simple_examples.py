"""
Example 1: Factorial  if n=0: n!=1
                      else: n! = n*(n-1)!
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


"""
Example 2: Cummulative sum. if n=0: sum(n) = 0 
                           else: sum(n) = n + sum(n-1)
           Ex. n = 4: sum(4) = 4 + 3 + 2 + 1 + 0 = 10
"""


def recersion_sum(n):
    if n == 0:
        return 0
    else:
        return n + recersion_sum(n - 1)


"""
Example 3: Given an integer, create a function which returns the sum of all the individual digits in that integer. 
           For example: if n = 4321, return 4+3+2+1
--> How to make it recursively
    '4321' = 1 + 432    = (4321//10  + 4321%10) 
           = 1 + 2 + 43 = 4321//10 + (432//10 + 432%10)
"""


def sum_func(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_func(n // 10)


"""
Example 4:
Create a function called word_split() which takes in a string phrase and a set list_of_words. 
The function will then determine if it is possible to split the string in a way in which words
can be made from the list of words. 
You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

For example:
word_split('themanran',['the','ran','man'])  =>  ['the', 'man', 'ran']
word_split('ilovedogsJohn', ['i','am','a','dogs','lover','love','John'])  => ['i', 'love', 'dogs', 'John']
word_split('themanran',['something','ran','man']) => []
"""


def word_split(phrase, predefine_words, output=None):
    if output is None:
        output = []  # because we will use this function recursively,
        # we should not make output=[] at the input arguments.
        # Otherwise, it will append the results when we run this function several times
        # for different phrase and predefine_words

    for word in predefine_words:
        if phrase.startswith(word):
            output.append(word)

            # Call function recursively with the reduction of phrase
            return word_split(phrase[len(word):], predefine_words, output)
        # End of if
    # End of for
    return output


if __name__ == "__main__":
    # Example 1
    n = 4
    print("Factorial of n = {} is {}".format(n, factorial(n)))  # 4!=24

    # Example 2
    n = 4
    print("recersion_sum of n = {} is {}".format(n, recersion_sum(n)))

    # Example 3
    n = 4321
    print("sum_func of n = {} is {}".format(n, sum_func(n)))  # 4321 = 4+3+2+1 = 10

    # Example 4
    print('output = {}'.format(word_split('themanran', ['the', 'ran', 'man'])))
    print('output = {}'.format(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John'])))
    print('output = {}'.format(word_split('themanran', ['something', 'ran', 'man'])))
