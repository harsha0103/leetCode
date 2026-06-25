# Last updated: 6/25/2026, 9:16:32 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root,curr_sum):
            if not root:
                return False

            if not root.left and not root.right:
                if curr_sum+root.val==targetSum:
                    return True
            
            left=dfs(root.left,curr_sum+root.val)
            right=dfs(root.right,curr_sum+root.val)
            if right or left:
                return True
            
            return False
        return dfs(root,0)