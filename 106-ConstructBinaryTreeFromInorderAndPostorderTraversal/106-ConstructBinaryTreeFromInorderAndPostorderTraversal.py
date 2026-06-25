# Last updated: 6/25/2026, 9:16:38 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(postorder)==0:
            return None
        
        val=postorder[-1]
        node=TreeNode(val)

        index=inorder.index(val)
        inorder_left=inorder[:index]
        inorder_right=inorder[index+1:]

        postorder_left=postorder[:len(inorder_left)]
        postorder_right=postorder[len(inorder_left):-1]

        node.left=self.buildTree(inorder_left, postorder_left)
        node.right=self.buildTree(inorder_right, postorder_right)

        return node