import pytest
from problems.decode_string import Solution


@pytest.mark.parametrize("s,expected", [
    ("", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("3[a]", "aaa"),
    ("3[a3[b]]", "abbbabbbabbb"),
    ("a3[b1[c]]", "abcbcbc"),
])
def test(s, expected):
    assert Solution().decodeString(s) == expected
