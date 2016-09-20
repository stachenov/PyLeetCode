import pytest
from problems.remove_element import Solution


@pytest.mark.parametrize("nums,val", [
    ([], 0),
    ([1], 0),
    ([1, 2], 1),
    ([1, 2, 1, 3], 1),
])
def test_removeElement(nums, val):
    expected = [n for n in nums if n != val]
    l = Solution().removeElement(nums, val)
    assert l == len(expected)
    assert nums[:l] == expected
