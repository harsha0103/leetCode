# Last updated: 6/25/2026, 9:16:58 AM
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
        res=head
        temp=head

        while res and temp:
            while temp and res.val==temp.val:
                temp=temp.next
            res.next=temp
            res=res.next
        return head
