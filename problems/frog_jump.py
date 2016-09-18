class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False
        can_jump = [set() for __ in xrange(len(stones))]
        can_jump[0] = {0}
        farthest = 1
        for i in xrange(1, len(stones)):
            if stones[i] > farthest:
                return False
            m = 0
            for j in xrange(i):
                d = stones[i] - stones[j]
                if d in can_jump[j] or d - 1 in can_jump[j] or d + 1 in can_jump[j]:
                    can_jump[i].add(d)
                    m = max(m, d + 1)
            farthest = max(farthest, stones[i] + m)
        return bool(can_jump[-1])
