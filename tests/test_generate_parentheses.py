import pytest
from problems.generate_parentheses import Solution


@pytest.mark.parametrize("n, expected", [
    (0, [""]),
    (1, ["()"]),
    (2, ["(())", "()()"]),
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
])
def test_generateParenthesis(n, expected):
    res = Solution().generateParenthesis(n)
    assert len(res) == len(expected)
    assert set(res) == set(expected)
