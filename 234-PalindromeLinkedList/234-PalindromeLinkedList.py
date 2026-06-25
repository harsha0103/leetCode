# Last updated: 6/25/2026, 9:15:05 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=head
        fast=head 

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=self.rev(slow,None)

        while head and prev:
            if head.val!=prev.val:
                return False
            head=head.next
            prev=prev.next
        
        if not prev:
            return True

        
    def rev(self,head,prev):
        if not head:
            return prev
        nxt=head.next
        head.next=prev
        return self.rev(nxt,head)