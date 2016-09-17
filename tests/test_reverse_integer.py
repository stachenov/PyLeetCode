import pytest
from problems.reverse_integer import Solution


@pytest.mark.parametrize("x,expected", [
    (0, 0),
    (1, 1),
    (12, 21),
    (-12, -21),
    (1000000003, 0),
])
def test(x, expected):
    assert Solution().reverse(x) == expected
