import pytest
from rotate_matrix import rotate_matrix, rotate_matrix_in_place


@pytest.mark.parametrize("fn", [rotate_matrix, rotate_matrix_in_place])
class TestShortInput:  # NxN where N = 1-9
    def test_1x1(self, fn):
        assert fn([[1]]) == [[1]]

    def test_2x2(self, fn):
        assert fn([[1, 2],
                   [3, 4]]) == [[3, 1],
                                [4, 2]]

    def test_3x3(self, fn):
        assert fn([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]) == [[7, 4, 1],
                                   [8, 5, 2],
                                   [9, 6, 3]]

    def test_4x4(self, fn):
        assert fn([[ 1,  2,  3,  4],
                   [ 5,  6,  7,  8],
                   [ 9, 10, 11, 12],
                   [13, 14, 15, 16]]) == [[13,  9,  5,  1],
                                          [14, 10,  6,  2],
                                          [15, 11,  7,  3],
                                          [16, 12,  8,  4]]


@pytest.mark.parametrize("fn", [rotate_matrix, rotate_matrix_in_place])
class TestMediumInput:  # NxN where N = 10-99
    def test_10x10(self, fn):
        n = 10
        matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        expected = [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]
        assert fn(matrix) == expected

    def test_50x50(self, fn):
        n = 50
        matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        expected = [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]
        assert fn(matrix) == expected


@pytest.mark.slow
@pytest.mark.parametrize("fn", [rotate_matrix, rotate_matrix_in_place])
class TestLongInput:  # NxN where N = 100+
    def test_100x100(self, fn):
        n = 100
        matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        expected = [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]
        assert fn(matrix) == expected

    def test_500x500(self, fn):
        n = 500
        matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
        expected = [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]
        assert fn(matrix) == expected


# Benchmark results (1,000 runs, per-run averages):
#
#                        rotate_matrix   rotate_matrix_in_place
# short  (4x4)           0.0054ms        0.0050ms
# medium (50x50)         0.3020ms        0.2964ms
# long   (500x500)      27.7272ms       28.1465ms
#
# Performance is nearly identical across all sizes. The in-place version avoids
# allocating a new matrix (O(1) vs O(n²) space) but the deepcopy overhead in
# benchmarking masks any allocation savings. In practice, in-place is preferred
# when mutation of the original is acceptable.
#
# Complexity:
#
#     | version                  | time  | space |
#     |--------------------------|-------|-------|
#     | rotate_matrix            | O(n²) | O(n²) |
#     | rotate_matrix_in_place   | O(n²) | O(1)  |
