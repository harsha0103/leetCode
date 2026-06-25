# Last updated: 6/25/2026, 9:17:00 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        res=head
        temp=head
        visited=set()

        while res and temp:
            count=0
            while temp and res.val==temp.val:
                if count==1:
                    visited.add(res.val)
                count+=1
                temp=temp.next
            res.next=temp
            res=res.next
        res=head
        while res and res.next:
            while res.next and res.next.val in visited:
                res.next=res.next.next
            
            res=res.next
        return head if head.val not in visited else head.next
