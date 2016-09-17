class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x > 0 and x % 10 == 0:
            return False
        # Original idea by @cbmbbz
        rev = 0
        while rev < x:
            rev *= 10
            rev += x % 10
            x /= 10
        return rev == x or rev / 10 == x
