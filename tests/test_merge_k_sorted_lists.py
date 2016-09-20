import pytest
from problems.merge_k_sorted_lists import Solution
from problems.classes import ListNode


@pytest.mark.parametrize("lists, expected", [
    ([], []),
    ([[]], []),
    ([[1]], [1]),
    ([[1], []], [1]),
    ([[1, 2], []], [1, 2]),
    ([[], [1, 2]], [1, 2]),
    ([[1], [2]], [1, 2]),
    ([[1, 2], [1, 2]], [1, 1, 2, 2]),
    ([[1, 2], [3, 4]], [1, 2, 3, 4]),
    ([[1, 4], [2, 3]], [1, 2, 3, 4]),
    ([[3, 4], [1, 2]], [1, 2, 3, 4]),
    ([[1, 3], [2]], [1, 2, 3]),
    ([[1, 4, 7], [2, 5], [3, 6]], [1, 2, 3, 4, 5, 6, 7]),
])
def test_mergeKLists(lists, expected):
    def convert(l):
        return ListNode(l) if l else None
    res = Solution().mergeKLists(map(convert, lists))
    if expected:
        assert list(res) == expected
    else:
        assert res is None
    res = Solution().mergeKLists_recursive(map(convert, lists))
    if expected:
        assert list(res) == expected
    else:
        assert res is None
