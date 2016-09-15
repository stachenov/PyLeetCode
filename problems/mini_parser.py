from classes import NestedInteger
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
import re


class Solution(object):
    eoi_re = re.compile(r"[,\]]")

    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        return self.deserialize_part(s, 0)[0]

    def deserialize_part(self, s, pos):
        if s[pos] == '[':
            ni = NestedInteger()
            i = pos + 1
            while i < len(s) and s[i] != ']':
                part = self.deserialize_part(s, i)
                ni.add(part[0])
                i = part[1]
                if s[i] == ',':
                    i += 1
            return ni, i + 1
        else:
            end = self.eoi_re.search(s, pos)
            end = end.start(0) if end else None
            return NestedInteger(int(s[pos:end])), end
