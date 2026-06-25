# Last updated: 6/25/2026, 9:14:07 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=[0]

        def dfs(root):
            if not root:
                return 
            
            if not root.left and not root.right:
                return root.val
            
            left=dfs(root.left)
            if left:
                res[0]+=left
            right=dfs(root.right)
        dfs(root)
        return res[0]