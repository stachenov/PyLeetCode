from itertools import product

import pytest
from problems.largest_divisible_subset import Solution

@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize("nums,expectedSize", [
    ([], 0),
    ([1, 2, 3], 2),
    ([1, 2, 4], 3),
    ([546, 669], 1),
    ([3, 4, 16, 8], 3),
])
def test(solution, nums, expectedSize):
    subset = solution.largestDivisibleSubset(nums)
    assert len(subset) == expectedSize
    assert is_divisible(subset)


def is_divisible(subset):
    return all(i % j == 0 or j % i == 0 for i, j in product(subset, subset))
