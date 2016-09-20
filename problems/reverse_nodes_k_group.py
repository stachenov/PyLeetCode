# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from problems.classes import ListNode


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse_k(node, force=False):
            new_tail, prev, n = node, None, 0
            for __ in xrange(k):
                n += 1
                next = node.next
                node.next = prev
                node, prev = next, node
                if not node:
                    break
            if n < k and not force:
                return reverse_k(prev, True)
            return prev, new_tail, next
        tail = dummy = ListNode(0)
        node = head
        while node:
            new_head, new_tail, node = reverse_k(node)
            tail.next = new_head
            tail = new_tail
        return dummy.next
