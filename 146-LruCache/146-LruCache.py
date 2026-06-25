# Last updated: 6/25/2026, 9:16:05 AM
class ListNode(object):
    def __init__(self,key=0,val=0,nxt=None,prev=None):
        self.key=key
        self.val=val
        self.next=nxt
        self.prev=prev

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.cache={}
        self.left,self.right=ListNode(),ListNode()
        self.left.next,self.right.prev=self.right,self.left
    
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        node.prev,node.next=prev,nxt
        prev.next,self.right.prev=node,node

    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
        node=ListNode(key,value)
        self.cache[key]=node
        self.insert(node)
        if len(self.cache)>self.cap:
            node=self.left.next
            del self.cache[node.key]
            self.remove(node)


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)