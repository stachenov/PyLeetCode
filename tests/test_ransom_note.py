import pytest
from problems.ransom_note import Solution


@pytest.mark.parametrize("note,magazine,expected", [
    ("a", "a", True),
    ("aa", "a", False),
    ("", "a", True),
    ("ab", "abc", True),
])
def test(note,magazine,expected):
    solution = Solution()
    assert solution.canConstruct(note, magazine) == expected
