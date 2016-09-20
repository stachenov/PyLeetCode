# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ahead = head
        for __ in xrange(n + 1):
            if ahead is None:
                return head.next
            ahead = ahead.next
        node = head
        while ahead is not None:
            node = node.next
            ahead = ahead.next
        node.next = node.next.next
        return head
