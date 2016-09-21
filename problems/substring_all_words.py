from collections import Counter


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        total_len = sum(map(len, words))
        if total_len > len(s) or not words:
            return []
        res = []
        word_count = Counter(words)
        def have_all(start):
            if not word_count:
                return True
            for w in word_count.keys():
                if s[start: start + len(w)] == w:
                    word_count[w] -= 1
                    if word_count[w] == 0:
                        del word_count[w]
                    if have_all(start + len(w)):
                        word_count[w] = word_count.get(w, 0) + 1
                        return True
                    word_count[w] = word_count.get(w, 0) + 1
        for start in xrange(0, len(s) - total_len + 1):
            if have_all(start):
                res.append(start)
        return res
