import pytest

from problems.random_pick_index import Solution


@pytest.mark.parametrize("nums", [
    ([1]),
    ([1, 2]),
    ([1, 1]),
])
def test(nums):
    solution = Solution(nums)
    sample = 100000
    values = {n for n in nums}
    for value in values:
        ind = []
        for i in xrange(0, sample):
            ind += [solution.pick(value)]
        count = float(len([v for v in nums if v == value]))
        c = dict((i, len([j for j in ind if j == i])) for i in set(ind))
        for i in c:
            assert nums[i] == value
            assert abs(c[i] / float(sample) - 1 / count) < 0.01
