from itertools import takewhile


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):
            b = data[i]
            ones = sum(1 for __ in (takewhile(lambda j: ((1 << j) & b) != 0, xrange(7, -1, -1))))
            size = 1 if ones == 0 else ones if 2 <= ones <= 7 else None
            if (size is None
                    or i + size > len(data)
                    or not all((0b11000000 & b) == 0b10000000 for b in data[i + 1: i + size])):
                return False
            i += size
        return True
