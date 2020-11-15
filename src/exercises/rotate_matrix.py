""" Rotate matrix by 90 degrees

Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.

Find more details on: https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
"""


def rotate_matrix(m, n):
    # Number of "squares" to rotate
    for i in range(int(n / 2)):
        # Rotate from outer to inner "square"
        for j in range(i, n - i - 1):
            temp = m[i][j]

            m[i][j] = m[j][n - 1 - i]
            m[j][n - 1 - i] = m[n - 1 - i][n - 1 - j]
            m[n - 1 - i][n - 1 - j] = m[n - 1 - j][i]
            m[n - 1 - j][i] = temp


def flatten_matrix(m, n):
    flat = [cell for row in m for cell in row]
    return " ".join(flat)


def print_matrix(m, n):
    print(flatten_matrix(m, n))
