# Last updated: 6/25/2026, 9:09:53 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=self.rev(slow,None)
        res=0

        while prev:
            res=max(head.val+prev.val,res)
            prev=prev.next
            head=head.next
        
        return res
    
    def rev(self,head,prev):
        if not head:
            return prev
        nxt=head.next
        head.next=prev
        return self.rev(nxt,head)