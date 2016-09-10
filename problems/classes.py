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