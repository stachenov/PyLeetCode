class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        m, start = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif stack:
                stack.pop()
                if stack:
                    m = max(m, i - stack[-1])
                else:
                    m = max(m, i + 1 - start)
            else:
                start = i + 1
        return m
