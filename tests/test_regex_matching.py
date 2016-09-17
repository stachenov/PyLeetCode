import pytest
from problems import regex_matching_dp, regex_matching_nfa


@pytest.mark.parametrize("s,p,expected", [
    ("", "", True),
    ("", ".*", True),
    ("", "a*", True),
    ("", "aa*", False),
    ("a", "", False),
    ("aa", "a", False),
    ("aa", "aa", True),
    ("aaa", "aa", False),
    ("aa", "a*", True),
    ("aa", ".*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("cccaaab", "c*a*b", True),
    ("cab", "c*a*b*", True),
    ("ab", "c*a*b*", True),
    ("cb", "c*a*b*", True),
    ("ca", "c*a*b*", True),
    ("ccb", "c*a*b*", True),
    ("aab", "c*a*b*", True),
    ("bb", "c*a*b*", True),
    ("cc", "c*a*b*", True),
    ("aa", "c*a*b*", True),
    ("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b", True),
])
def test(s, p, expected):
    assert regex_matching_dp.Solution().isMatch(s, p) == expected
    assert regex_matching_nfa.Solution().isMatch(s, p) == expected
