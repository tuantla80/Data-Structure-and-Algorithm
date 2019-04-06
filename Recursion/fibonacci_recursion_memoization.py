"""
Example 5. Fibonacci:   F(1) = 1
                        F(2) = 1
                        F(n) = F(n-1) + F(n-2)
Demonstrate:
    - Recursion
    - Memmoization:
      (Memoization is an optimization technique used primarily to speed up computer programs
       by storing the previous results).
    - Solve with NON recursion
"""

# Recursion
def fibonacci(n):
    """
    Solved using recursion
    Ex. for n in range(1, 101):
            print(n, ":", fibonacci(n)

    BUT when n>30, it will be too SLOW. Because it is recursive function so it will refer to the previous one.
    And the larger n number, the bigger number steps it has to recursive call.
    => Need memoization (refer to function below)
    """
    assert isinstance(n, int) and n>=1, "n should be positive integer"

    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Recursion with memoization
fibonacci_catch = {}  # store the function call
def fibonacci_with_memoization(n):
    """
    Solved using recursion with memoization
    Ex. for n in range(1, 101):
            print(n, ":", fibonacci_with_memoization(n)
    - Memoization: catch values so the future call do not repeat the work
    - Method: (1) Using memoization explicitly
              (2) Using builtin Python tool
    """
    assert isinstance(n, int) and n >= 1, "n should be positive integer"

    # Check if the value of fibonacci(n) has stored in catch
    if n in fibonacci_catch.keys():
        return fibonacci_catch(n)

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # Catch the value and then return it
    fibonacci_catch[n]=value
    print('fibonacci_catch ', fibonacci_catch)
    return value


# Recursion with lru_cache (memoization)
from functools import lru_cache
@lru_cache(maxsize=128)  # by defaul, Python chose 128 recently values
def fibonacci_with_lru_cache(n):
    assert isinstance(n, int) and n>=1, "n should be positive integer"

    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# With NON recursion solution
def fibonacci_NON_recursion_solution(n):
    a = 1
    b = 1
    for i in range(n-1):  # choose n-1 since we assume n=1 return 1
        a, b = b, a+b
    return a

if __name__=="__main__":

    print("\nFibonacci with recursion")
    for n in range(1, 10): # when n > 30, it is so slow
        print(n, ":", fibonacci(n))

    print("\nFibonacci with recursion and mmemoization")
    for n in range(1, 101):
        print(n, ":", fibonacci_with_memoization(n))

    print("\nFibonacci with recursion and lru_cache (mmemoization)")
    for n in range(1, 101):
        print(n, ":", fibonacci_with_lru_cache(n))

    print("\nFibonacci with NON recursion solution")
    for n in range(1, 101):
        print(n, ":", fibonacci_NON_recursion_solution(n))