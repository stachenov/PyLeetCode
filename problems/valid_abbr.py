class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = j = 0
        while j < len(abbr):
            if abbr[j].isdigit():
                count = int(abbr[j])
                j += 1
                if count == 0:
                    return False
                while j < len(abbr) and abbr[j].isdigit():
                    count *= 10
                    count += int(abbr[j])
                    j += 1
                i += count
            elif abbr[j] == word[i]:
                i += 1
                j += 1
            else:
                return False
            if i >= len(word):
                return i == len(word) and j == len(abbr)
        return i == len(word)
