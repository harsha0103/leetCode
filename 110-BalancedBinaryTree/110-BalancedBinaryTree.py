# Last updated: 6/25/2026, 9:16:34 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):
            
            if not root:
                return (0,True)
            
            left_height,left_b= dfs(root.left)
            right_height,right_b = dfs(root.right)

            curr_b=left_b and right_b and abs(left_height-right_height)<=1
            curr_h=1+max(left_height,right_height)

            return (curr_h,curr_b)
        
        return dfs(root)[1]