class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        end = 0
        while True:
            if end > len(strs[0]):
                break
            p = strs[0][:end]
            def have_p(s): return end <= len(s) and s[:end] == p
            if not all(have_p(s) for s in strs[1:]):
                break
            end += 1
        return strs[0][:end - 1]
