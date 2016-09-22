import pytest
from problems.jump_game_2 import Solution


@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], 2),
    ([10, 3, 1, 1, 4], 1),
    ([2, 1, 1, 1, 4], 3),
])
def test_jump(nums, expected):
    assert Solution().jump(nums) == expected
