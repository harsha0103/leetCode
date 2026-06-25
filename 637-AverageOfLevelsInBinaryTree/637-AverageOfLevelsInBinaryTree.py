# Last updated: 6/25/2026, 9:13:07 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        q=deque([root])
        l=len(q)
        temp=[]
        res=[]
        while q:
            if l==0:
                t_res=float(sum(temp))/len(temp)
                res.append(t_res)
                l=len(q)
                temp=[]
            l-=1
            curr=q.popleft()
            temp.append(curr.val)
            if curr.left:
                q.append(curr.left)
            
            if curr.right:
                q.append(curr.right)
            
        t_res=float(sum(temp))/len(temp)
        res.append(t_res)
        return res