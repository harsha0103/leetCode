# Last updated: 6/25/2026, 9:12:46 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        if root.val==val:
            return root
        
        left=self.searchBST(root.left, val)
        if left:
            return left
        right=self.searchBST(root.right, val)
        if right:
            return right
    


