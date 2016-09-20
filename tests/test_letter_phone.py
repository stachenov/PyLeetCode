import pytest
from problems.letter_phone import Solution


@pytest.mark.parametrize("digits,expected", [
    ("", []),
    ("2", ["a", "b", "c"]),
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
])
def test_letterCombinations(digits, expected):
    combinations = Solution().letterCombinations(digits)
    assert len(combinations) == len(expected)
    assert set(combinations) == set(expected)
