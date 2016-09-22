class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def solve(sofar, candidates, target):
            if target == 0:
                res.append(sofar)
                return
            if not candidates:
                return
            for i, c in enumerate(candidates):
                if c > target:
                    break
                solve(sofar + [c], candidates[i:], target - c)
        solve([], candidates, target)
        return res
