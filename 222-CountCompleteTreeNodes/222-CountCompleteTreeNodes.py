# Last updated: 6/25/2026, 9:15:11 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # stack=[root] if root else []
        # cou=0
        # while stack:
        #     current=stack.pop()
        #     if current:
        #         cou+=1
        #     if current.left:
        #         stack.append(current.left)
        #     if current.right:
        #         stack.append(current.right)
        # return cou

        if root is None:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return 1+left+right


