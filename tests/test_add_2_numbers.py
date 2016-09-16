import pytest
from problems.add_2_numbers import Solution
from problems.classes import ListNode


@pytest.mark.parametrize("l1,l2,expected", [
    ([2], [2], [4]),
    ([2], [2, 1], [4, 1]),
    ([2], [8, 1], [0, 2]),
    ([9, 9, 9], [1], [0, 0, 0, 1]),
])
def test(l1, l2, expected):
    assert list(Solution().addTwoNumbers(ListNode(l1), ListNode(l2))) == list(expected)
