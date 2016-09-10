import pytest

from problems.classes import ListNode
from problems.plus_one_linked_list import Solution

@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize("head,expected", [
    (ListNode([0]), [1]),
    (ListNode([9]), [1, 0]),
    (ListNode([1, 9]), [2, 0]),
    (ListNode([9, 1, 9]), [9, 2, 0]),
])
def test(solution, head, expected):
    assert [n for n in solution.plusOne(head)] == expected
