# Last updated: 6/25/2026, 9:18:02 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        prev,nxt=ListNode(0,head),head

        dummy=prev
        while n>0:
            n-=1
            nxt=nxt.next
        
        while nxt:
            prev=prev.next
            nxt=nxt.next
        
        prev.next=prev.next.next

        return dummy.next