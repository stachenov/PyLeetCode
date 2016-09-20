import pytest
from problems.valid_parentheses import Solution


@pytest.mark.parametrize("s,expected", [
    ("()", True),
    ("(", False),
    (")", False),
    ("([])", True),
    ("([)]", False),
])
def test_isValid(s, expected):
    assert Solution().isValid(s) is expected
