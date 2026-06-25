# Last updated: 6/25/2026, 9:16:22 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q=[(root,root.val)] if root else None
        res=0
        while q:
            curr,curr_val=q.pop()
            if not curr.left and not curr.right:
                res=res+curr_val
            
            if curr.left:
                q.append((curr.left,curr_val*10+curr.left.val))
            
            if curr.right:
                q.append((curr.right,curr_val*10+curr.right.val))
        
        return res
