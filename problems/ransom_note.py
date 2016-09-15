from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c = Counter(magazine)
        c.subtract(Counter(ransomNote))
        return all(v >= 0 for v in c.values())
