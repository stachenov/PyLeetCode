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
        wc = Counter(words)
        wl = len(words[0])
        res = []
        for shift in xrange(0, wl):
            i, j = shift, shift
            while i <= len(s) - wl:
                if j - i < total_len and j <= len(s) - wl and wc.get(s[j: j + wl], 0) > 0:
                    wc[s[j: j + wl]] -= 1
                    if wc[s[j: j + wl]] == 0:
                        del wc[s[j: j + wl]]
                        if not wc:
                            res.append(i)
                    j += wl
                elif j - i > 0:
                    wc[s[i: i + wl]] = wc.get(s[i: i + wl], 0) + 1
                    i += wl
                else:
                    i, j = i + wl, j + wl
        return res
