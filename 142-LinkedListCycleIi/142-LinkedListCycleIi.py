# Last updated: 6/25/2026, 9:16:10 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        
        if not fast or not fast.next:
            return None
        while head and slow:
            if slow==head:
                return head
            slow=slow.next
            head=head.next