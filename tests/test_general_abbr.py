import pytest
from problems.general_abbr import Solution


@pytest.mark.parametrize("word, expected", [
    ("ab", ["2", "a1", "1b", "ab"]),
    ("abc", ["3", "a2", "1b1", "2c", "ab1", "1bc", "a1c", "abc"]),
    ("word", ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]),
])
def test_generateAbbreviations(word, expected):
    abbrs = Solution().generateAbbreviations(word)
    assert len(abbrs) == len(expected)
    assert set(abbrs) ==  set(expected)
