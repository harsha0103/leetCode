# Last updated: 6/25/2026, 9:18:29 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res=ListNode()
        curr=res
        borrow=0

        while l1 and l2:
            total=l1.val+l2.val+borrow
            borrow=total//10
            curr.next=ListNode(total%10)
            curr=curr.next

            l1=l1.next
            l2=l2.next

        while l1:
            total=borrow+l1.val
            borrow=total//10
            curr.next=ListNode(total%10)
            curr=curr.next

            l1=l1.next
        
        while l2:
            total=borrow+l2.val
            borrow=total//10
            curr.next=ListNode(total%10)
            curr=curr.next

            l2=l2.next

        if borrow>0:
            curr.next=ListNode(borrow)
        
        return res.next