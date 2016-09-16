from itertools import count


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
        start = self.find_cycle(a)
        period, powa = self.compute_powers(a, start)
        if reversed(b) < ((start // 10 ** p) % 10 for p in count()):
            return powa[self.mod(b, start)]
        else:
            return powa[start] * powa[self.mod(self.subtract(b, start), period)] % 1337

    @staticmethod
    def find_cycle(a):
        # Floyd's Tortoise and the Hare algorithm
        slow = 1
        fast = 1
        while True:
            slow = slow * a % 1337
            fast = fast * a * a % 1337
            if slow == fast:
                break
        finder = 1
        pow = 0
        while slow != finder:
            pow += 1
            slow = slow * a % 1337
            finder = finder * a % 1337
        return pow

    @staticmethod
    def compute_powers(a, start):
        powa = [1]
        for i in xrange(1, 1337):
            powa.append(powa[i - 1] * a % 1337)
            if i > start and powa[i] == powa[start]:
                period = i - start
                break
        return period, powa

    @staticmethod
    def subtract(b, c):
        borrow = 0
        for i in xrange(len(b) - 1, -1, -1):
            if b[i] - borrow < c % 10:
                b[i] = b[i] - borrow - c % 10 + 10
                borrow = 1
            else:
                b[i] -= c % 10 + borrow
            c //= 10
            if c == 0:
                break
        return b

    @staticmethod
    def mod(b, period):
        m = 0
        for d in b:
            m = (m * 10 + d) % period
        return m
