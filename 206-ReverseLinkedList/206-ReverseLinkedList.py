# Last updated: 6/25/2026, 9:15:27 AM

from sys import _current_frames# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self._reverseList(head,None)
    
    def _reverseList(self,head,prev):

        if not head:
            return prev
        
        ne=head.next
        head.next=prev
        return self._reverseList(ne,head)


