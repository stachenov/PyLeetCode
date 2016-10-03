import re

import pytest
from problems.min_abbr import Solution


@pytest.mark.parametrize("target, dictionary, exp_len", [
    ("apple", ["blade"], 2),
    ("apple", ["plain", "amber", "blade"], 3),
    ("abc", ["bbc", "adc", "abb"], 3),
    ("abc", ["bbc", "xxx", "yyy"], 2),
    ("abc", ["xxx", "xxx", "yyy"], 2),
    ("abc", ["a", "b", "c"], 1),
    ("abcd", ["abcx", "xbcd", "axcd", "abxd"], 4),
    ("abcd", ["abcx", "xbcd", "axcd"], 4),
    ("abcd", ["abcx", "xbcd"], 3),
    ("abcd", ["abcx"], 2),
    ("a", ["b"], 1),
])
def test_minAbbreviation(target, dictionary, exp_len):
    abbr = Solution().minAbbreviation(target, dictionary)
    assert len(abbr) == exp_len
    assert re.compile("^" + re.sub(r"[1-9]\d*", lambda m: ".{" + m.group() + "}", abbr) + "$").match(target)
