def permute(s):
    """
    Problem:
    Given a string, write a function that uses recursion to
    output a list of all the possible permutations of that string.
    For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    NOTE: we can use permutation in itertools library
         https://docs.python.org/2/library/itertools.html#itertools.permutations
    """
    output = []

     # Base case
    if len(s) <=1:
        output = [s]
    else:
        # Run for every letter in string s
        for i, letter in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                output += [letter + perm]
    return output

if __name__=="__main__":
    output = permute(s='abc')
    print(list(set(output)))