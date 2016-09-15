class ListNode(object):
    def __init__(self, x):
        if type(x) is list:
            self.val = x[0]
            node = self
            for n in x[1:]:
                node.next = ListNode(n)
                node = node.next
            node.next = None
        else:
            self.val = x
            self.next = None

    def __iter__(self):
        node = self
        while node is not None:
            yield node.val
            node = node.next


class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.content = value if value else []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return type(self.content) is int

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.content.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.content = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.content

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.content

    def __str__(self):
        if self.isInteger():
            return str(self.content)
        else:
            return "[" + ",".join(map(str, self.content)) + "]"
