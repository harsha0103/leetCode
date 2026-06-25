# Last updated: 6/25/2026, 9:17:59 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1=list1
        head2=list2
        res=ListNode()
        curr=res
        while head1 and head2:
            if head1.val>= head2.val:
                curr.next=head2
                head2=head2.next
            else:
                curr.next=head1
                head1=head1.next
            curr=curr.next
        
        while head1:
            curr.next=head1
            curr=curr.next
            head1=head1.next
        
        while head2:
            curr.next=head2
            curr=curr.next
            head2=head2.next
        
        return res.next
            
