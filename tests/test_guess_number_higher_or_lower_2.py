import pytest

from problems import guess_number_higher_or_lower
from problems.guess_number_higher_or_lower_2 import Solution


@pytest.mark.parametrize("n,money", [
    (1, 0),
    (2, 1),
    (4, 4),
])
def test(n, money):
    solution = Solution()
    assert solution.getMoneyAmount(n) == money
