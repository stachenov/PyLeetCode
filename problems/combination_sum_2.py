class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def solve(sofar, cnd, target):
            if target == 0:
                res.append(sofar)
                return
            if not cnd:
                return
            i = 0
            while i < len(cnd):
                c = cnd[i]
                if c > target:
                    break
                solve(sofar + [c], cnd[i + 1:], target - c)
                while i + 1 < len(cnd) and cnd[i + 1] == cnd[i]:
                    i += 1
                i += 1

        solve([], sorted(candidates), target)
        return res
