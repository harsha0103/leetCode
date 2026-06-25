# Last updated: 6/25/2026, 9:16:33 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=[float('inf')]
        def dfs(root):
            if not root:
                return 0
            

            
            left=dfs(root.left)
            right=dfs(root.right)

            if not root.left:
                return 1+right
            
            elif not root.right:
                return 1+left
            
            else:


                return 1+min(left,right)
        
        return dfs(root)
          