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

    def mergeKLists_recursive(self, lists, start=None, end=None):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if start is None: start = 0
        if end is None: end = len(lists)
        if end - start == 0:
            return None
        elif end - start == 1:
            return lists[start]
        else:
            dummy = ListNode(0)
            tail = dummy
            mid = (start + end) / 2
            l1 = self.mergeKLists_recursive(lists, start, mid)
            l2 = self.mergeKLists_recursive(lists, mid, end)
            while l1 or l2:
                if not l1 or l2 and l2.val < l1.val:
                    tail.next = l2
                    l2 = l2.next
                else:
                    tail.next = l1
                    l1 = l1.next
                tail = tail.next
            return dummy.next
