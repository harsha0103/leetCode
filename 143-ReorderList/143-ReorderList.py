# Last updated: 6/25/2026, 9:16:09 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next

        prev=slow.next
        second_half=slow.next=None
        slow=prev
        while slow:
            prev=slow.next
            slow.next=second_half
            second_half=slow
            slow=prev
        

        first,second= head, second_half
        while second:
            temp1,temp2=first.next,second.next
            first.next=second
            first=first.next
            first.next=temp1
            first=first.next
            second=temp2



  


        
    