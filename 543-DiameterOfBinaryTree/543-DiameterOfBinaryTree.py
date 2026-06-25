# Last updated: 6/25/2026, 9:13:44 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        m=[0]
        def dfs(root):
            if not root:
                return 0
                
            left=dfs(root.left)
            right=dfs(root.right)

            m[0]=max(m[0],left+right)
            return 1+ max(left,right)
        
        dfs(root)
        return m[0]