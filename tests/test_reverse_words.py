import pytest
from problems.reverse_words import Solution


@pytest.mark.parametrize("s, expected", [
    ("", ""),
    ("a", "a"),
    ("a b", "b a"),
    ("ab bc", "bc ab"),
])
def test_reverseWords(s, expected):
    assert Solution().reverseWords(s) == expected
