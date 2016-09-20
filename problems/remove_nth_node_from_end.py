from classes import ListNode

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
        dummy = ListNode(0)
        dummy.next = head
        ahead = dummy
        for __ in xrange(n + 1):
            ahead = ahead.next
        node = dummy
        while ahead is not None:
            node, ahead = node.next, ahead.next
        node.next = node.next.next
        return dummy.next
