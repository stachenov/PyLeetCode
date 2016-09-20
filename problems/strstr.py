class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        kmp = [0] * len(needle)
        i, j = 0, 1
        while j + 1 < len(needle):
            if needle[j] == needle[i]:
                kmp[j + 1] = i + 1
                i, j = i + 1, j + 1
            elif i > 0:
                i = kmp[i]
            else:
                j += 1
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
                if j == len(needle):
                    return i - j
            elif j > 0:
                j = kmp[j]
            else:
                i += 1
        return -1
