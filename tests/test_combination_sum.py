import pytest
from problems.combination_sum import Solution


@pytest.mark.parametrize("candidates, target, expected", [
    ([2, 3, 6, 7], 7, [
        [2, 2, 3],
        [7],
    ]),
    ([1], 1, [
        [1],
    ]),
    ([1], 2, [
        [1, 1],
    ]),
    ([1, 2], 3, [
        [1, 1, 1],
        [1, 2],
    ]),
    ([8, 7, 4, 3], 11, [[3, 4, 4], [3, 8], [4, 7]]),
])
def test_combinationSum(candidates, target, expected):
    assert Solution().combinationSum(candidates, target) == expected
