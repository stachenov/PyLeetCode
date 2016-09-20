import pytest
from problems.strstr import Solution


@pytest.mark.parametrize("haystack, needle", [
    ("", ""),
    ("ab", "a"),
    ("ab", "b"),
    ("aa", "a"),
    ("aab", "ab"),
    ("aaab", "aab"),
    ("caab", "aab"),
    ("caabc", "aabc"),
    ("aabaaba", "aaba"),
    ("ababcdxyabababcxyabdd", "ababcxyab"),
    ("abaabcxyab", "ababcxyab"),
    ("ababcxyabcxyad", "ababcxyad"),
])
def test_strStr(haystack, needle):
    expected = haystack.find(needle)
    assert Solution().strStr(haystack, needle) == expected
