import itertools
import pytest
from problems.shuffle_array import Solution


@pytest.mark.parametrize("nums", [
    ([1]),
    ([1, 2]),
])
def test(nums):
    copy = list(nums)
    solution = Solution(nums)
    sample_size = 10000
    permutations = []
    for __ in xrange(sample_size):
        permutation = solution.shuffle()
        assert set(permutation) == set(copy)
        permutations.append(permutation)
    for i, n in itertools.product(xrange(len(copy)), copy):
        count_n_at_i = sum(1 for p in permutations if p[i] == n)
        assert abs(count_n_at_i / float(sample_size) - 1.0 / len(copy)) < 0.01
    assert solution.reset() == copy
