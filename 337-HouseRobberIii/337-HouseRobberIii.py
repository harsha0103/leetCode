# Last updated: 6/25/2026, 9:14:20 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
    
        def dfs(root):
            if not root:
                return (0,0)
        
            left=dfs(root.left)
            right=dfs(root.right)

            with_root=root.val+left[1]+right[1]
            without_root= max(left)+max(right)

            return (with_root,without_root)

        return max(dfs(root))