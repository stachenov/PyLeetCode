import re


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Original idea by @StefanPochmann
        r = re.compile(r"(\d+)\[([^\d\[\]]*)\]")
        while r.search(s):
            s = r.sub(lambda m: int(m.group(1)) * m.group(2), s)
        return s
