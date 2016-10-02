import re


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        return bool(re.match("^" + re.sub(r"[1-9]\d*", lambda c: ".{" + c.group() + "}", abbr) + "$", word))
