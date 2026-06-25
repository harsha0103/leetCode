# Last updated: 6/25/2026, 9:16:45 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root:
            q=deque([root]) 
        else:
            return []
        level=1
        temp=[]
        res=[]

        while q:
            if level==0:
                res.append(temp)
                temp=[]
                level=len(q)
            level-=1
            curr=q.popleft()
            temp.append(curr.val)

            if curr.left:
                q.append(curr.left)
            
            if curr.right:
                q.append(curr.right)
        
        res.append(temp)

        return res