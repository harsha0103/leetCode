# Last updated: 6/25/2026, 9:16:27 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.total=float('-inf')
        def dfs(root):
            if not root:
                return 0

            left=dfs(root.left)
            right=dfs(root.right)
            max_left=max(left,0)
            max_right=max(right,0)
            self.total=max(self.total,root.val+max_left+max_right)
            return root.val +max(max_left,max_right)
        
        dfs(root)
        return self.total