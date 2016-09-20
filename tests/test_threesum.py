import pytest
from problems.threesum import Solution


@pytest.mark.parametrize("nums,expected", [
    ([-1, 0, 1, 2, -1, -4], [
        (-1, 0, 1),
        (-1, -1, 2),
    ]),
    ([], []),
    ([0], []),
    ([0, 0], []),
    ([0, 0, 0], [
        (0, 0, 0),
    ]),
    ([1, 2, 3], [
    ]),
    ([1, 1, -2], [
        (-2, 1, 1),
    ]),
    ([-2, 1, 1], [
        (-2, 1, 1),
    ]),
    ([1, -2, 1], [
        (-2, 1, 1),
    ]),
    ([0, 0, 0, -1, 0, 1, -2, 1, 1, 1, -3, 2, 2, -4, 2, 3, 3, -6], [
        (0, 0, 0),
        (-1, 0, 1),
        (-2, 1, 1),
        (-3, 1, 2),
        (-4, 2, 2),
        (-6, 3, 3),
        (-4, 1, 3),
        (-2, -1, 3),
        (-2, 0, 2),
        (-3, 0, 3),
    ]),
    ([-10, 1, 2, 5, 5], [
        (-10, 5, 5),
    ]),
    ([-10, -1, 0, 2, 10], [
        (-10, 0, 10),
    ])
])
def test_threeSum(nums, expected):
    list_of_lists = Solution().threeSum(nums)
    assert len(list_of_lists) == len(expected)
    assert set(map(tuple, list_of_lists)) == set(expected)
