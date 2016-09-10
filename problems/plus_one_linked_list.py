from problems.classes import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last_not_9, head = self.find_last_not_9(head)
        last_not_9.val += 1
        node = last_not_9.next
        while node is not None:
            node.val = 0
            node = node.next
        return head

    @staticmethod
    def find_last_not_9(head):
        last_not_9 = None
        node = head
        while node is not None:
            if node.val != 9:
                last_not_9 = node
            node = node.next
        if last_not_9 is None:
            last_not_9 = ListNode(0)
            last_not_9.next = head
            head = last_not_9
        return last_not_9, head
