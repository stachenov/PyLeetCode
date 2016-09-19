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
            for j1 in incoming_jumps[stone]:
                for j2 in xrange(max(j1 - 1, 1), j1 + 2):
                    if stone + j2 in stones_set:
                        incoming_jumps[stone + j2].add(j2)
        return bool(incoming_jumps[stones[-1]])

    def canCross_topDown(self, stones):
        # Original idea by @AlgoGuruZ, code mine
        stones_set = set(stones)
        known = {}
        def canCross(s1, s2):
            if (s1, s2) not in known:
                if s2 == stones[-1]:
                    known[s1, s2] = True
                else:
                    d2 = s2 - s1
                    known[s1, s2] = any(canCross(s2, s2 + d3) for d3
                                        in xrange(max(d2 - 1, 1), d2 + 2)
                                        if s2 + d3 in stones_set)
            return known[s1, s2]
        return canCross(0, 0)
