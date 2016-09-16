from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Editorial approach #3
        i, j, indices, answer = 0, 0, defaultdict(lambda: -1), 0
        for j, c in enumerate(s):
            i = max(i, indices[c] + 1)
            answer = max(answer, j + 1 - i)
            indices[c] = j
        return answer
