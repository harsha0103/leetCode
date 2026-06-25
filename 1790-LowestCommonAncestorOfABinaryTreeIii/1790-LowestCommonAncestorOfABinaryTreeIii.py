# Last updated: 6/25/2026, 9:10:20 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        res_p=[]
        res_q=[]
        while p:
            res_p.append(p)
            p=p.parent
        while q:
            res_q.append(q)
            q=q.parent
        res=0
        while res_p and res_q:
            curr_p, curr_q=res_p.pop(),res_q.pop()
            if curr_p!=curr_q:
                break
            res=curr_p
        return res