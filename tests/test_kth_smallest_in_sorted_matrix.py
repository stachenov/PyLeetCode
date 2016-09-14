import pytest
from problems.kth_smallest_in_sorted_matrix import Solution


@pytest.mark.parametrize("matrix,k,expected", [
    ([
         [1, 5, 9],
         [10, 11, 13],
         [12, 13, 15]
     ], 8, 13),
    ([
         [1, 5, 9],
         [10, 11, 13],
         [12, 13, 15]
     ], 3, 9),
])
def test(matrix, k, expected):
    solution = Solution()
    assert solution.kthSmallest(matrix, k) == expected
