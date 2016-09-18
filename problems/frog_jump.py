from collections import defaultdict


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        stones_set = set(stones)
        incoming_jumps = defaultdict(set)
        incoming_jumps[1] = {1}
        for stone in stones[1:]:
            for jump in incoming_jumps[stone]:
                for d in xrange(-1 if jump > 1 else 0, +2):
                    if stone + jump + d in stones_set:
                        incoming_jumps[stone + jump + d].add(jump + d)
        return bool(incoming_jumps[stones[-1]])

    def canCross_topDown(self, stones):
        # Original idea by @AlgoGuruZ, code mine
        if stones[1] != 1:
            return False
        stones_set = set(stones)
        known = {}
        def canCross(s1, s2):
            if (s1, s2) not in known:
                if s2 == stones[-1]:
                    known[(s1, s2)] = True
                else:
                    d = s2 - s1
                    known[(s1, s2)] = any(canCross(s2, s3) for s3
                                          in xrange(s2 + d - 1 if d > 1 else s2 + d, s2 + d + 2)
                                          if s3 in stones_set)
            return known[(s1, s2)]
        return canCross(0, 1)
