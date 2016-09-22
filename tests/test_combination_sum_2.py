import pytest
from problems.combination_sum_2 import Solution


@pytest.mark.parametrize("candidates, target, expected", [
    ([2, 3, 6, 7], 7, [
        [7],
    ]),
    ([1], 1, [
        [1],
    ]),
    ([1], 2, [
    ]),
    ([1, 2], 3, [
        [1, 2],
    ]),
    ([8, 7, 4, 3], 11, [[3, 8], [4, 7]]),
    ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
])
def test_combinationSum2(candidates, target, expected):
    assert Solution().combinationSum2(candidates, target) == expected
