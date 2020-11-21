"""
Find more details at: https://www.geeksforgeeks.org/coin-change-dp-7/
"""


def __solve_coin_change(denominations, amount, sequence, results):
    """
    Function to solve coin change

    :param denominations: (list) List of denominations. I.e: different coin amounts
    :param amount: (int) Amount to resolve
    :param sequence: (list) Current list of denominations used to solve the amount
    """
    if not denominations:
        return

    den = denominations[-1]
    if den == amount:
        # If current denomination resolves the amount, store as result
        results.append(sequence + [den])

    elif den < amount:
        # If current denomination is smaller than the amount, substract to the amount
        # and add to the sequence of denominations used to solve the amount
        __solve_coin_change(denominations, amount - den, sequence + [den], results)

    # Try to resolve the amount without the current denomination
    __solve_coin_change(denominations[:-1], amount, sequence, results)


def solve_coin_change(denominations, amount):
    """
    Function to solve coin change

    :param denominations: (list) List of denominations. I.e: different coin amounts
    :param amount: (int) Amount to resolve
    :returns: (list(list)) List of lists with the different solve coin possibilities
    """
    options = []
    __solve_coin_change(denominations, amount, [], options)
    return options
