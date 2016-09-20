import pytest
from problems.remove_nth_node_from_end import Solution
from problems.classes import ListNode


@pytest.mark.parametrize("head,n,expected", [
    ([1], 1, []),
    ([1, 2], 1, [1]),
    ([1, 2], 2, [2]),
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
])
def test_removeNthFromEnd(head, n, expected):
    new_head = Solution().removeNthFromEnd(ListNode(head), n)
    if expected:
        assert list(new_head) == expected
    else:
        assert new_head is None
