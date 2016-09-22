class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) < sum(1 for c in p if c != '*'):
            return False
        match = [True]
        for c in p:
            match.append(match[-1] and c == '*')
        for cs in s:
            prev = match
            match = [False]
            for j, cp in enumerate(p):
                match.append(match[j] and cp == '*'
                             or prev[j + 1] and cp == '*'
                             or prev[j] and (cp == '?' or cp == cs))
        return match[len(p)]
