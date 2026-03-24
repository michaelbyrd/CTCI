# Chapter 1 | Arrays and Strings
# Problem 1.7 — Rotate Matrix
#
# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
#
# Example (clockwise rotation):
#   Input:          Output:
#   1 2 3           7 4 1
#   4 5 6    ->     8 5 2
#   7 8 9           9 6 3
#
# Why transpose + reverse each row = 90° clockwise rotation:
#
#   Step 1 — Transpose (flip along the diagonal, [r][c] → [c][r]):
#     1 2 3          1 4 7
#     4 5 6    →     2 5 8
#     7 8 9          3 6 9
#
#   Step 2 — Reverse each row:
#     1 4 7          7 4 1
#     2 5 8    →     8 5 2
#     3 6 9          9 6 3
#
#   Why it works: after a 90° clockwise rotation, the left column becomes the top
#   row — but reversed. The transpose moves each column into a row (right elements,
#   wrong order). Reversing each row fixes the order.


# Time: O(n²), Space: O(n²)
def rotate_matrix(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n)]

    # Step 1 — Transpose
    for row in range(n):
        for col in range(n):
            result[col][row] = matrix[row][col]

    # Step 2 — Reverse each row
    for row in result:
        row.reverse()
    return result


# Time: O(n²), Space: O(1)
def rotate_matrix_in_place(matrix):
    n = len(matrix)

    # Step 1 — Transpose (only upper triangle to avoid double-swapping)
    for row in range(n):
        for col in range(row + 1, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    # Step 2 — Reverse each row
    for row in matrix:
        row.reverse()
    return matrix


# Tuple unpacking eliminates the need for a swap variable: the right-hand side
# is evaluated fully first (both values captured in a temporary tuple), then
# unpacked into the left-hand side. The temporary tuple is the implicit swap.

# using swap variable
# swap = matrix[col][row]
# matrix[col][row] = matrix[row][col]
# matrix[row][col] = swap

# using temporary tuple
# matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

# Upper triangle explained
# [ X    O    O    O ]
# [ 5    X    O    O ]
# [ 9   10    X    O ]
# [13   14   15    X ]
# Diagonal Xs are ignored, no need to transpose
# 'Upper triangle' swaps(O) will adjust the 'Lower triangle' positions
