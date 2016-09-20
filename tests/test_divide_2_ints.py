import pytest
from problems.divide_2_ints import Solution


@pytest.mark.parametrize("dividend, divisor", [
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2),
    (4, 2),
    (4, 3),
    (8, 1),
    (8, 2),
    (8, 3),
    (8, 4),
    (8, 5),
    (8, 6),
    (8, 7),
    (8, 8),
    (2 ** 31 - 1, 1),
    (2 ** 31 - 1, 2),
    (15, 3),
    (15, 4),
    (15, 5),
    (-1, 1),
    (-2 ** 31, -2 ** 31),
    (-2 ** 31, 2 ** 31 - 1),
    (-2 ** 31, -1),
])
def test_divide(dividend, divisor):
    res = Solution().divide(dividend, divisor)
    if divisor == 0:
        assert res == 2 ** 31 - 1
    else:
        quot = abs(dividend) / abs(divisor)
        if dividend < 0 < divisor or divisor < 0 < dividend:
            quot = -quot
        if -2 ** 31 <= quot <= 2 ** 31 - 1:
            assert res == quot
        else:
            assert res == 2 ** 31 - 1
