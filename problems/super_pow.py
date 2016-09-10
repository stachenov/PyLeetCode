class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        self.cache10 = {}
        c = 1
        for d in enumerate(reversed(b)):
            c *= self.pow10(a ** d[1] % 1337, d[0])
            c %= 1337
        return c

    def pow10(self, a, mul10):
        if (a, mul10) in self.cache10:
            return self.cache10[a, mul10]
        if mul10 == 0:
            self.cache10[a, 0] = a
        elif mul10 == 1:
            self.cache10[a, 1] = a ** 10 % 1337
        else:
            self.cache10[a, mul10] = self.pow10(self.pow10(a, mul10 // 2) % 1337,
                                                mul10 - mul10 // 2) % 1337
        return self.cache10[a, mul10]
