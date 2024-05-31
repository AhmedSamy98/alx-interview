#!/usr/bin/python3
"""
    Module: Rotate 2D Matrix in 90 Degrees
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise
    """
    for i in range(int(len(matrix) / 2)):
        for j in range(i, (len(matrix) - i - 1)):
            m = (len(matrix) - 1 - j)
            mcopy = matrix[i][j]
            matrix[i][j] = matrix[m][i]
            matrix[m][i] = matrix[(len(matrix) - i - 1)][m]
            matrix[(len(matrix) - i - 1)][m] = matrix[j][(len(matrix) - i - 1)]
            matrix[j][(len(matrix) - i - 1)] = mcopy
