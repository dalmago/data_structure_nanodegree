# You are given coins of different denominations and a total amount of money.
# Write a function to compute the fewest coins needed to make up that amount.

def coin_change(coins, amount):
    # This should return one value: the fewest coins needed to make up the given amount

    # Create a memo that will store the fewest coins with given amount
    # that we have already calculated so that we do not have to do the
    # calculation again.
    memo = {}

    def recursive_helper(change):
        if change < 0:
            return float('inf')
        if change == 0:
            return 0

        if change not in memo:
            memo[change] = min(recursive_helper(change - coin) + 1 for coin in coins)

        return memo[change]

    res = recursive_helper(amount)
    return -1 if res == float('inf') else res


def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)

arr = [1,4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)
