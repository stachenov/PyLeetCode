class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # money[size][start] is how much we need to guess a number in the
        # start (inclusive) ... start + size (exclusive) range
        money = [[0] * (n + 2)] * 2 # don't need money to guess 0 or 1 number

        def left_part_size(guess, start):
            return guess - start

        def right_part_size(guess, start, size):
            return size - left_part_size(guess, start) - 1

        for size in xrange(2, n + 1):
            money.append([0])
            max_start = n + 1 - size
            for start in xrange(1, max_start + 1):
                money[size].append(min(guess + max(money[left_part_size(guess, start)][start],
                                                   money[right_part_size(guess, start, size)][guess + 1])
                                       for guess in xrange(start, start + size)))
        return money[n][1]
