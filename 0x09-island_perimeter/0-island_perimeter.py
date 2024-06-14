#!/usr/bin/python3
"""
    Module: Function that Computes the perimeter of an island
"""


def island_perimeter(grid):
    """
        Computes the perimeter of an island described by a Grid

        Input: List of Lists
        Returns: Perimeter of the island
    """
    p = 0
    gd_len = len(grid)
    for row in range(gd_len):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                if row - 1 < 0 or grid[row - 1][column] == 0:
                    p += 1
                if column - 1 < 0 or grid[row][column - 1] == 0:
                    p += 1
                if column + 1 >= len(grid[row]) or grid[row][column + 1] == 0:
                    p += 1
                if row + 1 >= gd_len or grid[row + 1][column] == 0:
                    p += 1
    return p
