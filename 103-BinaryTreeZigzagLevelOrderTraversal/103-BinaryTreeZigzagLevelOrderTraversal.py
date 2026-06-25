# Last updated: 6/25/2026, 9:16:44 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=deque([root])
        level=len(q)
        temp=deque()
        res=[]
        odd=True
        while q:
            if level==0:
                res.append(temp)
                odd= not odd    
                temp=deque()
                level=len(q)
            level-=1
            curr=q.popleft()
            if odd:
                temp.append(curr.val)
            else:
                temp.appendleft(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        res.append(temp)
        res1=[]
        for i in res:
            res1.append(list(i))
        return res1