import pytest
from problems.nth_digit import Solution


@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (10, 1),
    (11, 0),
    (12, 1),
    (100, 5),
    (189, 9),
    (190, 1),
    (191, 0),
    (192, 0),
    (193, 1),
    (194, 0),
    (195, 1),
    (195, 1),
    (2887, 9),
    (2888, 9),
    (2889, 9),
    (2890, 1),
    (2891, 0),
    (2892, 0),
    (2893, 0),
    (2894, 1),
    (2895, 0),
    (2896, 0),
    (2897, 1),
])
def test_findNthDigit(n, expected):
    assert Solution().findNthDigit(n) == expected
