# Last updated: 6/25/2026, 9:17:55 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr1=ListNode(0,head)
        prev1=curr1
        curr=head
        while curr:
            k_node=self.group(curr,k)
            if not k_node:
                break
            k_nxt=k_node.next
            new_head=self.reverse(curr,k_node.next,k_nxt)
            prev1.next=new_head
            prev1=curr
            curr=k_nxt

        return curr1.next
    
    def reverse(self,head,prev,k_next):
        if  head==k_next:
            return prev
        nxt=head.next
        head.next=prev
        return self.reverse(nxt,head,k_next)
    
    def group(self,head,k):
        while head and k>1:
            head=head.next
            k-=1
        return head