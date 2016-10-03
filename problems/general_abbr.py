class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def generate(abbr, pos):
            if pos == len(word):
                yield abbr
            else:
                if not abbr or not abbr[-1].isdigit():
                    for i in xrange(pos + 1, len(word) + 1):
                        for res in generate(abbr + str(i - pos), i):
                            yield res
                for res in generate(abbr + word[pos:pos + 1], pos + 1):
                    yield res
        return [w for w in generate("", 0)]
