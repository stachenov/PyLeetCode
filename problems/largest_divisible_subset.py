class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        parent = {-1: -1}
        length = {-1: -1}
        for i in xrange(0, len(nums)):
            parent[nums[i]] = max((d for d in length if nums[i] % d == 0), key=lambda d: length[d])
            length[nums[i]] = length[parent[nums[i]]] + 1

        def seq():
            num = max(length, key=lambda n: length[n])
            while num != -1:
                yield num
                num = parent[num]

        return list(seq())