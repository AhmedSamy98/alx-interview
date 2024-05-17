#!/usr/bin/python3
"""
    This Module Contains a funcion to validate utf-8
    Author: Ahmed Samy
"""


def validUTF8(data):
    """
    This funciton validates utf-8
    """
    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b00000000

    def count_leading_ones(byte):
        count = 0
        mask = 0b10000000
        while (byte & mask) == mask:
            count += 1
            mask >>= 1
        return count

    i = 0
    while i < len(data):
        leading_ones = count_leading_ones(data[i])
        if leading_ones == 0:
            i += 1
        else:
            if leading_ones == 1 or leading_ones > 4 or i + \
                    leading_ones > len(data):
                return False

            for j in range(1, leading_ones):
                if not (data[i + j] & 0b11000000) == 0b10000000:
                    return False

            i += leading_ones

    return True
