# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from problems.classes import ListNode


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        tail = dummy
        first, second = head, head.next
        while first and second:
            next_first = second.next
            next_second = next_first.next if next_first else None
            tail.next = second
            tail = tail.next
            tail.next = first
            tail = tail.next
            first, second = next_first, next_second
        if first:
            tail.next = first
            tail = tail.next
        tail.next = None
        return dummy.next
