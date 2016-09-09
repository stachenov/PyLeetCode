class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        parent = {-1: -1}
        length = {-1: -1}
        for num in nums:
            parent[num] = max((d for d in length if num % d == 0),
                              key=lambda d: length[d])
            length[num] = length[parent[num]] + 1

        def seq():
            num = max(length.iteritems(), key=lambda n: n[1])[0]
            while num != -1:
                yield num
                num = parent[num]

        return list(seq())
