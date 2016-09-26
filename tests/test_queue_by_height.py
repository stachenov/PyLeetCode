import pytest
from problems.queue_by_height import Solution


@pytest.mark.parametrize("people, expected", [
    ([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
     [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]),
])
def test_reconstructQueue(people, expected):
    assert Solution().reconstructQueue(people) == expected
