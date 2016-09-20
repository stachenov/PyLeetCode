class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if not (c == ')' and p == '(' or c == ']' and p == '[' or c == '}' and p == '{'):
                    return False
        return not stack
