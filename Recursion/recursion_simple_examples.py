"""
Example 1: Factorial  if n=0: n!=1
                      else: n! = n*(n-1)!
"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

"""
Example 2: Cummulative sum. if n=0: sum(n) = 0 
                           else: sum(n) = n + sum(n-1)
           Ex. n = 4: sum(4) = 4 + 3 + 2 + 1 + 0 = 10
"""
def recersion_sum(n):
    if n == 0:
        return 0
    else:
        return n + recersion_sum(n-1)

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
        return n%10 + sum_func(n//10)


if __name__ == "__main__":
    n = 4
    print("Factorial of n = {} is {}".format(n, factorial(n)))  # 4!=24
    print("recersion_sum of n = {} is {}".format(n, recersion_sum(n)))

    n = 4321
    print("sum_func of n = {} is {}".format(n, sum_func(n)))  # 4321 = 4+3+2+1 = 10
