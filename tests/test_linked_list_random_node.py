import pytest

from problems.classes import ListNode
from problems.linked_list_random_node import Solution


@pytest.mark.parametrize("head", [
    ([1]),
    ([2]),
    ([1, 2]),
])
def test(head):
    solution = Solution(ListNode(head))
    size = sum(1 for __ in head)
    sample_size = 100000
    nums = [solution.getRandom() for __ in xrange(0, sample_size)]
    for n in set(nums):
        c = sum(1 for i in nums if i == n)
        p = c / float(sample_size)
        assert abs(p - sum(1 for i in head if i == n) / float(size)) < 0.01
