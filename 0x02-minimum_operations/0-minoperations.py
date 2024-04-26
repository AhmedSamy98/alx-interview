#!/usr/bin/python3

"""
Module: Minimum Operations
"""


def minOperations(n):
    """
    A method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file
    If n is impossible to achieve, returns 0
    """
    if not isinstance(n, int):
        return 0

    ops = 0
    iterr = 2
    while (iterr <= n):
        if not (n % iterr):
            n = int(n / iterr)
            ops += iterr
            iterr = 1
        iterr += 1
    return ops
