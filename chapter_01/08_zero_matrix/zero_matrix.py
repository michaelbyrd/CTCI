# Chapter 1 | Arrays and Strings
# Problem 1.8 — Zero Matrix
#
# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.
#
# Example:
#   Input:            Output:
#   1  2  3           1  0  3
#   4  0  6    ->     0  0  0
#   7  8  9           7  0  9


# Time: O(M*N), Space: O(M+N)
def zero_matrix(matrix):
    rows, cols = set(), set()
    x, y = len(matrix), len(matrix[0])
    # find all 0s, store in arrays
    for row in range(x):
        for col in range(y):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    for row in range(x):
        for col in cols:
            matrix[row][col] = 0

    for row in rows:
        matrix[row] = [0] * y

    return matrix
