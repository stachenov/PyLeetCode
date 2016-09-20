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
        kmp[0] = -1
        if len(needle) > 1:
            kmp[1] = 0
        i, j = 0, 1
        while j + 1 < len(needle):
            if needle[j] == needle[i]:
                kmp[j + 1] = i + 1
                i, j = i + 1, j + 1
            elif kmp[i] >= 0:
                i = kmp[i]
            else:
                assert i == 0
                j += 1
        i, j = 0, 0
        while i + j < len(haystack):
            if haystack[i + j] == needle[j]:
                j += 1
                if j == len(needle):
                    return i
            elif kmp[j] >= 0:
                i += j - kmp[j]
                j = kmp[j]
            else:
                i, j = i + 1, 0
        return -1
