# Last updated: 6/25/2026, 9:12:11 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        stack=[root]
        res=root.val    
        while stack:
            current = stack.pop()
            if res!=current.val:
                return False
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return True