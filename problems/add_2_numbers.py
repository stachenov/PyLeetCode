from classes import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            n1, n2 = (l1.val if l1 else 0), (l2.val if l2 else 0)
            n = n1 + n2 + carry
            carry = n / 10
            n %= 10
            tail.next = ListNode(n)
            tail = tail.next
            l1, l2 = (l1.next if l1 else None), (l2.next if l2 else None)
        return dummy.next
