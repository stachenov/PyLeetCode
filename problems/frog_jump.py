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
