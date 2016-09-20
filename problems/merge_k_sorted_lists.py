# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from classes import ListNode
from heapq import heapify, heappop, heappush


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [(l.val, i, l) for i, l in enumerate(lists) if l is not None]
        heapify(heap)
        dummy = ListNode(0)
        tail = dummy
        while heap:
            l = heappop(heap)
            tail.next = l[2]
            tail = tail.next
            if l[2].next is not None:
                heappush(heap, (l[2].next.val, l[1], l[2].next))
        return dummy.next
