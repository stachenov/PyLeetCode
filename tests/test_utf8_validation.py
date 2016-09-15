import pytest
from problems.utf8_validation import Solution


@pytest.mark.parametrize("data,expected", [
    ([0], True),
    ([0b10000000], False),
    ([0b11000000], False),
    ([0b11000000, 0b10000000], True),
    ([0b11100000, 0b10000000, 0b10000000], True),
    ([0b11110000, 0b10000000, 0b10000000, 0b10000000], True),
    ([0b11111000, 0b10000000, 0b10000000, 0b10000000, 0b10000000], True),
    ([0b11111100, 0b10000000, 0b10000000, 0b10000000, 0b10000000, 0b10000000], True),
    ([0b11111110, 0b10000000, 0b10000000, 0b10000000, 0b10000000, 0b10000000, 0b10000000], True),
    ([0b11111110, 0b10000000, 0b10000000, 0b10000000, 0b10000000, 0b10000000], False),
    ([0b11111111], False),
])
def test(data, expected):
    solution = Solution()
    assert solution.validUtf8(data) == expected
