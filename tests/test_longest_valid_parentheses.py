import pytest
from problems.longest_valid_parentheses import Solution


@pytest.mark.parametrize("s, expected", [
    ("", 0),
    (")(", 0),
    ("()", 2),
    ("(())", 4),
    ("()()", 4),
    ("(()()", 4),
    (")()()", 4),
    ("()())()", 4),
    ("()(())", 6),
])
def test_longestValidParentheses(s, expected):
    assert Solution().longestValidParentheses(s) == expected
