#!/usr/bin/python3
"""module for the function makeChange"""


def makeChange(coins, total):
    """the fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0

    coins = sorted(coins)[::-1]
    count = 0
    for coin in coins:
        if total <= 0:
            break
        while total >= coin:
            total -= coin
            count += 1
    if total:
        return -1
    return count
