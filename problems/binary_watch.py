class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        def decode(b):
            h = b >> 6
            m = b & 0b111111
            if h <= 11 and m <= 59:
                hh = str(h)
                mm = str(m)
                if len(mm) == 1:
                    mm = "0" + mm
                res.append(hh + ":" + mm)
        def read_bits(n, b, m):
            if n == 0:
                decode(b)
            else:
                for i in xrange(m, 10):
                    if (b & (1 << i)) == 0:
                        read_bits(n - 1, b | (1 << i), i + 1)
        read_bits(num, 0, 0)
        return res
