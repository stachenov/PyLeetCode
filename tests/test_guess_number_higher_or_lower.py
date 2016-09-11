import pytest

from problems import guess_number_higher_or_lower
from problems.guess_number_higher_or_lower import Solution


@pytest.mark.parametrize("k,n", [
    (1, 1),
    (1, 2),
])
def test(k, n):
    solution = Solution()
    def guess(m):
        if k == m:
            return 0
        elif k < m:
            return -1
        else:
            return +1
    guess_number_higher_or_lower.guess = guess
    assert solution.guessNumber(n) == k
