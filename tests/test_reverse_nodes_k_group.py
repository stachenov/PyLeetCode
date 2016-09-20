import pytest

from problems.classes import ListNode
from problems.reverse_nodes_k_group import Solution


@pytest.mark.parametrize("head, k, expected", [
    ([], 1, []),
    ([], 2, []),
    ([1], 2, [1]),
    ([1, 2], 2, [2, 1]),
    ([1, 2, 3], 2, [2, 1, 3]),
    ([1, 2, 3], 3, [3, 2, 1]),
    ([1, 2, 3, 4], 3, [3, 2, 1, 4]),
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [3, 2, 1, 6, 5, 4, 7]),
    ([1, 2, 3, 4, 5, 6], 4, [4, 3, 2, 1, 5, 6]),
    ([1, 2, 3, 4, 5, 6, 7], 4, [4, 3, 2, 1, 5, 6, 7]),
])
def test_reverseKGroup(head, k, expected):
    res = Solution().reverseKGroup(ListNode(head) if head else None, k)
    if expected:
        assert list(res) == expected
    else:
        assert res is None
