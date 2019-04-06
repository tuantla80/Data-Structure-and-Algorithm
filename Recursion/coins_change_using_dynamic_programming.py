"""
Problem:
Given a target amount n and a list (array) of distinct coin values,
what's the fewest coins needed to make the change amount.

For example:
    If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:
    1+1+1+1+1+1+1+1+1+1
    5 + 1+1+1+1+1
    5+5
    10
    With 1 coin being the minimum amount.
"""

def coins_change_dynamic(target, coins, known_results):
    """
    Using dynamic programming (memoization)
    """

    # Default output for the target
    min_coins = target

    # base case
    if target in coins:
        known_results[target] = 1
        return 1

    # Return a known_results (already calculated) if it happens to be >=1
    elif known_results[target] > 0:
        return known_results[target]

    else:
        # For every coin <= target
        for i in [coin for coin in coins if coin <= target]:
            num_coins = 1 + coins_change_dynamic(target-i, coins, known_results)
            if num_coins < min_coins:
                min_coins = num_coins

                # reset known_results
                known_results[target] = min_coins

    return min_coins

if __name__=="__main__":
    target = 100
    coins = [1, 5, 10, 25]
    known_results = [0]*(target+1)

    min_coins = coins_change_dynamic(target, coins, known_results)
    print("min_coins = ", min_coins)

















