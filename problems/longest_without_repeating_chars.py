class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        chars = set()
        answer = 0
        while i < len(s):
            while j < len(s) and not s[j] in chars:
                chars.add(s[j])
                j += 1
            answer = max(answer, j - i)
            if j == len(s):
                break
            k = s.index(s[j], i)
            chars -= set(s[i:k])
            i, j = k + 1, j + 1
        return answer
