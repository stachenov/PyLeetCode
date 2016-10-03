import re


class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        dictionary = [w for w in dictionary if len(w) == len(target)]
        if not dictionary:
            return str(len(target))
        matches = [set() for __ in xrange(len(target))]
        for i, c in enumerate(target):
            for w in dictionary:
                if w[i] == c:  # add to set of words matching target at pos i
                    matches[i].add(w)
        re_num = re.compile(r"(?:\d+|\D+)")
        if not any(matches):  # we must leave at least one char to distinguish the abbr
            return target if len(target) == 1 else target[0] + str(len(target) - 1)

        def matching(abbr):
            i, s = 0, set()
            for p in re_num.findall(abbr):
                if p[0].isdigit():
                    i += int(p)  # skip wildcard
                else:  # non-wildcard part
                    for j in xrange(len(p)):
                        if s:
                            s &= matches[i + j]
                            if not s:  # intersection of all matching sets will be empty too
                                return s
                        else:  # first set, or all previous were empty
                            s = set(matches[i + j])  # copy to avoid modifications in matches
                    i += len(p)
            return s

        def generate(abbr, pos, remove):
            if remove == 0:
                yield abbr + target[pos:]
            else:
                start = 0 if pos == 0 else pos + 1  # skip 1 char to avoid generating adjacent numbers
                for i in xrange(start, len(target) - remove):
                    for r in xrange(1, remove + 1):  # decrease length by r (replace r + 1 chars with 1 number)
                        for res in generate(abbr + target[pos:i] + str(r + 1), i + r + 1, remove - r):
                            yield res

        for L in xrange(2, len(target) + 1):
            for abbr in generate("", 0, len(target) - L):
                if not matching(abbr):
                    return abbr
