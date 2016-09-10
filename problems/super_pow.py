class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        a %= 1337
        if a == 0:
            return 0
        powa = []
        period = 1338
        c = a
        for i in xrange(0, 1337):
            powa.append(c)
            c = c * a % 1337
            if c == a:
                period = i + 1
                break
        modb = self.mod(b, period)
        return powa[period - 1 if modb == 0 else modb - 1]

    @staticmethod
    def mod(b, period):
        m = 0
        for d in b:
            m = (m * 10 + d) % period
        return m
