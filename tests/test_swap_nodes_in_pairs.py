import pytest

from problems.classes import ListNode
from problems.swap_nodes_in_pairs import Solution


@pytest.mark.parametrize("head,expected", [
    ([], []),
    ([1], [1]),
    ([1, 2], [2, 1]),
    ([1, 2, 3], [2, 1, 3]),
    ([1, 2, 3, 4], [2, 1, 4, 3]),
])
def test_swapPairs(head, expected):
    res = Solution().swapPairs(ListNode(head) if head else None)
    if expected:
        assert list(res) == expected
    else:
        assert res is None
