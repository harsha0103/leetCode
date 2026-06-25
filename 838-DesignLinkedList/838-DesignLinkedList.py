# Last updated: 6/25/2026, 9:12:32 AM
class ListNode(object):

    def __init__(self,val=0,nxt=None,prev=None):
        self.val=val
        self.next=nxt
        self.prev=prev


class MyLinkedList(object):

    def __init__(self):
        self.left,self.right=ListNode(),ListNode()
        self.left.next,self.right.prev=self.right,self.left



    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr=self.left.next
        while curr and index>0:
            curr=curr.next
            index-=1
        if curr and index==0 and self.right!=curr:

            return curr.val
        return -1


    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        nxt,prev=self.left.next,self.left
        node=ListNode(val)
        prev.next,nxt.prev=node,node
        node.prev,node.next=prev,nxt


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        prev,nxt=self.right.prev,self.right
        node=ListNode(val)
        prev.next,nxt.prev=node,node
        node.prev,node.next=prev,nxt
        
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        curr=self.left.next
        while curr and index>0:
            index-=1
            curr=curr.next
        if curr and index==0:
            prev=curr.prev
            nxt= curr
            node=ListNode(val)
            prev.next,nxt.prev=node,node
            node.prev,node.next=prev,nxt

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """

        curr=self.left.next
        while curr and index>0:
            index-=1
            curr=curr.next
        if curr and self.right!=curr and index==0:
            prev=curr.prev
            nxt= curr.next 
            prev.next,nxt.prev=nxt,prev

    




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)