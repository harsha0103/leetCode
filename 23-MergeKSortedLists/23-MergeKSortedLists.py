# Last updated: 6/25/2026, 9:17:56 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        while len(lists)>1:
            new_list=[]
            for i in range(0,len(lists),2):
                a=lists[i]
                b=lists[i+1] if i+1<len(lists)  else None 
                e=self.merge(a,b)
                new_list.append(e)
            lists=new_list
            
        
        res=lists.pop() if len(lists)>0 else None 
        return res


    
    def merge(self,list1,list2):
        node=ListNode(0)
        dummy=node
        while list1 and list2:
            if list1.val >list2.val:
                node.next=list2
                list2=list2.next
            else:
                node.next=list1
                list1=list1.next
            node=node.next
        if list1:
            node.next=list1
        if list2:
            node.next=list2

        return dummy.next


                