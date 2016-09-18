class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        def read_bits(numbits, mask, numbit):
            if numbits == 0:
                if (mask >> 6) <= 11 and (mask & 0b111111) <= 59:
                    res.append("%d:%02d" % (mask >> 6, mask & 0b111111))
            else:
                for i in xrange(numbit, 10):
                    if (mask & (1 << i)) == 0:
                        read_bits(numbits - 1, mask | (1 << i), i + 1)
        read_bits(num, 0, 0)
        return res
