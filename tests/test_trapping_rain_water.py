import pytest
from problems.trapping_rain_water import Solution


@pytest.mark.parametrize("height, expected", [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([5, 0, 5], 5),
    ([5, 0, 0, 5], 10),
    ([0, 5, 5, 0], 0),
    ([5, 0, 5, 0, 5], 10),
    ([5, 0, 10, 0, 5], 10),
    ([1, 0, 10, 0, 5], 6),
])
def test_trap(height, expected):
    assert Solution().trap(height) == expected
    assert Solution().trap_2pointers(height) == expected
