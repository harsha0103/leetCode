# Last updated: 6/25/2026, 9:16:37 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root:
            q=deque([root]) 
        else:
            return []

        l=len(q)
        tres=[]
        res=deque([])
        while q:
            if l==0:
                l=len(q)
                res.appendleft(tres)
                tres=[]
            current=q.popleft()
            tres.append(current.val)
            l-=1
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        res.appendleft(tres)

        return list(res)