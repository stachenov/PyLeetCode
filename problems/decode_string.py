class Solution(object):
    def decodeString(self, s, pos=0):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        i = pos
        while i < len(s):
            if '0' <= s[i] <= '9':
                sub_pos = s.index('[', i)
                rep = int(s[i: sub_pos])
                dec = self.decodeString(s, sub_pos + 1)
                res += rep * dec[0]
                i = dec[1] + 1
            elif s[i] == ']':
                return res, i
            else:
                res += s[i]
                i += 1
        return res
