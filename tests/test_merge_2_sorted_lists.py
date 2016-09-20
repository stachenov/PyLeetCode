import pytest
from problems.merge_2_sorted_lists import Solution
from problems.classes import ListNode


@pytest.mark.parametrize("l1, l2, expected", [
    ([], [], []),
    ([1], [], [1]),
    ([], [1], [1]),
    ([1], [2], [1, 2]),
    ([2], [1], [1, 2]),
    ([1, 2], [3, 4], [1, 2, 3, 4]),
    ([3, 4], [1, 2], [1, 2, 3, 4]),
    ([1, 4], [2, 3], [1, 2, 3, 4]),
    ([1, 3], [2, 4], [1, 2, 3, 4]),
])
def test_mergeTwoLists(l1, l2, expected):
    l3 = Solution().mergeTwoLists(ListNode(l1) if l1 else None, ListNode(l2) if l2 else None)
    if not expected:
        assert l3 is None
    else:
        assert list(l3) == expected
