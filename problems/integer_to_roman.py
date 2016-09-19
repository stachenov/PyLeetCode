class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman_digits = [(), (1,), (1, 1), (1, 1, 1), (1, 5),
                        (5,), (5, 1), (5, 1, 1), (5, 1, 1, 1), (1, 10)]
        letters = [{1: 'I', 5: 'V', 10: 'X'},
                   {1: 'X', 5: 'L', 10: 'C'},
                   {1: 'C', 5: 'D', 10: 'M'},
                   {1: 'M'}]
        res = ""
        for pos, digit in enumerate(reversed(map(int, str(num)))):
            res = ''.join(map(lambda d: letters[pos][d], roman_digits[digit])) + res
        return res
