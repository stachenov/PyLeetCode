from problems import integer_to_roman
from problems.roman_to_integer import Solution


def test_romanToInt():
    for i in xrange(1, 4000):
        r = integer_to_roman.Solution().intToRoman(i)
        assert Solution().romanToInt(r) == i
