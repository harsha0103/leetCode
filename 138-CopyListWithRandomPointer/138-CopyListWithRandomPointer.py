# Last updated: 6/25/2026, 9:16:14 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        d={None:None}
        temp=head
        while temp:
            d[temp]=Node(temp.val)
            temp=temp.next
        temp1=head
        while temp1:
            nxt=temp1.next
            rand=temp1.random
            d[temp1].next=d[nxt]
            d[temp1].random=d[rand]
            temp1=temp1.next
        return d[head]

            
