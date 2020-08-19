import collections


# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])


def knapsack_max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """

    # Initialize a lookup table to store the maximum value ($)
    memoization = [0] * knapsack_max_weight

    # Iterate down the given list
    for item in items:

        # The "capcacity" represents amount of remaining capacity (kg) of knapsack at a given moment.
        for capacity in range(knapsack_max_weight - 1, item.weight - 2, -1):
            not_pick_value = memoization[capacity]
            pick_value = item.value + (memoization[capacity - item.weight] if capacity - item.weight > 0 else 0)

            memoization[capacity] = max(pick_value, not_pick_value)

    return memoization[-1]

tests = [
    {
        'correct_output': 14,
        'input': {
            'knapsack_max_weight': 15,
            'items': [Item(10, 7), Item(9, 8), Item(5, 6)]
        }
    },
    {
        'correct_output': 13,
        'input': {
            'knapsack_max_weight': 25,
            'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]
        }
    }
]

for test in tests:
    assert test['correct_output'] == knapsack_max_value(**test['input'])
    print("ok")
