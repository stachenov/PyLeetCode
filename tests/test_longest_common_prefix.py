import pytest
from problems.longest_common_prefix import Solution


@pytest.mark.parametrize("strs,expected", [
    ([], ""),
    ([""], ""),
    (["a", "b"], ""),
    (["a", "a"], "a"),
    (["ab", "abc", "ad"], "a"),
])
def test_longestCommonPrefix(strs, expected):
    assert Solution().longestCommonPrefix(strs) == expected
