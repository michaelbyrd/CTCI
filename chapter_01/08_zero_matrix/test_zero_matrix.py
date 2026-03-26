import pytest
from zero_matrix import zero_matrix


@pytest.mark.parametrize("fn", [zero_matrix])
class TestShortInput:  # MxN where M,N = 1-9
    def test_1x1_no_zero(self, fn):
        assert fn([[1]]) == [[1]]

    def test_1x1_zero(self, fn):
        assert fn([[0]]) == [[0]]

    def test_2x2_no_zero(self, fn):
        assert fn([[1, 2],
                   [3, 4]]) == [[1, 2],
                                [3, 4]]

    def test_2x2_one_zero(self, fn):
        assert fn([[1, 0],
                   [3, 4]]) == [[0, 0],
                                [3, 0]]

    def test_3x3_one_zero(self, fn):
        assert fn([[1, 2, 3],
                   [4, 0, 6],
                   [7, 8, 9]]) == [[1, 0, 3],
                                   [0, 0, 0],
                                   [7, 0, 9]]

    def test_3x3_two_zeros(self, fn):
        assert fn([[1, 0, 3],
                   [4, 5, 6],
                   [0, 8, 9]]) == [[0, 0, 0],
                                   [0, 0, 6],
                                   [0, 0, 0]]

    def test_3x3_no_zero(self, fn):
        assert fn([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]) == [[1, 2, 3],
                                   [4, 5, 6],
                                   [7, 8, 9]]

    def test_non_square(self, fn):
        assert fn([[1, 0, 3],
                   [4, 5, 6]]) == [[0, 0, 0],
                                   [4, 0, 6]]


@pytest.mark.parametrize("fn", [zero_matrix])
class TestMediumInput:  # MxN where M,N = 10-99
    def test_10x10_no_zero(self, fn):
        n = 10
        matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        assert fn(matrix) == matrix

    def test_10x10_one_zero(self, fn):
        n = 10
        matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        matrix[3][5] = 0
        result = fn(matrix)
        assert all(result[3][c] == 0 for c in range(n))
        assert all(result[r][5] == 0 for r in range(n))

    def test_50x50_no_zero(self, fn):
        n = 50
        matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        assert fn(matrix) == matrix

    def test_50x50_one_zero(self, fn):
        n = 50
        matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        matrix[10][20] = 0
        result = fn(matrix)
        assert all(result[10][c] == 0 for c in range(n))
        assert all(result[r][20] == 0 for r in range(n))


@pytest.mark.slow
@pytest.mark.parametrize("fn", [zero_matrix])
class TestLongInput:  # MxN where M,N = 100+
    def test_100x100_one_zero(self, fn):
        n = 100
        matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        matrix[50][50] = 0
        result = fn(matrix)
        assert all(result[50][c] == 0 for c in range(n))
        assert all(result[r][50] == 0 for r in range(n))

    def test_500x500_one_zero(self, fn):
        n = 500
        matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        matrix[100][200] = 0
        result = fn(matrix)
        assert all(result[100][c] == 0 for c in range(n))
        assert all(result[r][200] == 0 for r in range(n))


# Benchmark results (1,000 runs, per-run averages):
#
#                          zero_matrix
# short  (3x3)             0.0039ms
# medium (50x50)           0.2915ms
# long   (500x500)        25.9491ms
#
# Complexity:
#
#     | version     | time    | space   |
#     |-------------|---------|---------|
#     | zero_matrix | O(M*N)  | O(M+N)  |
#
#     M = rows, N = cols
#     Space: O(M+N) to store the zero row/col indices
