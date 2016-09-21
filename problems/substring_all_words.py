from collections import defaultdict
from functools import partial


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        indexes = defaultdict(partial(defaultdict, list))
        for n, w in enumerate(words):
            i = 0
            while i < len(s):
                j = s.find(w, i)
                if j == -1:
                    break
                indexes[w][n].append(j)
                i = j + 1
            if not indexes[w][n]:
                return []
        def have_all(start):
            if not any(indexes.values()):
                return True
            if start == len(s):
                return False
            for w in indexes.keys():
                for n in indexes[w].keys():
                    w_indexes = indexes[w][n]
                    if start in w_indexes:
                        del indexes[w][n]
                        if have_all(start + len(w)):
                            indexes[w][n] = w_indexes
                            return True
                        indexes[w][n] = w_indexes
        res = []
        for w in indexes.keys():
            n = indexes[w].keys()[0]
            w_indexes = indexes[w][n]
            del indexes[w][n]
            for i in w_indexes:
                if have_all(i + len(w)):
                    res.append(i)
            indexes[w][n] = w_indexes
        return sorted(res)
