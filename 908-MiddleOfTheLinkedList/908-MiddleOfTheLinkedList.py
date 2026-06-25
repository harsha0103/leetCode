# Last updated: 6/25/2026, 9:12:23 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast=head
        while fast and fast.next:
            head=head.next
            fast=fast.next.next
        return head