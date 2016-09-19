import pytest
from problems.integer_to_roman import Solution


@pytest.mark.parametrize("num,expected", [
    (1, "I"),
    (2, "II"),
    (4, "IV"),
    (6, "VI"),
    (9, "IX"),
    (90, "XC"),
    (99, "XCIX"),
    (100, "C"),
    (1000, "M"),
    (11, "XI"),
])
def test_intToRoman(num, expected):
    assert Solution().intToRoman(num) == expected
