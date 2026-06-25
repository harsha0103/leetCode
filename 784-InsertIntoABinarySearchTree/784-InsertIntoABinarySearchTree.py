# Last updated: 6/25/2026, 9:12:45 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)

        if val<root.val:
            left=self.insertIntoBST(root.left,val)
            root.left=left
        
        else:
            right=self.insertIntoBST(root.right,val)
            root.right=right
        
        return root