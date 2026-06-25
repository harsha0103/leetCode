# Last updated: 6/25/2026, 9:16:41 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder)==0:
            return None
        
        val=preorder[0]
        node=TreeNode(val)

        index=inorder.index(val)
        inorder_left=inorder[:index]
        inorder_right=inorder[index+1:]

        preorder_left=preorder[1:len(inorder_left)+1]
        preorder_right=preorder[len(inorder_left)+1:]

        node.left=self.buildTree(preorder_left,inorder_left)
        node.right=self.buildTree(preorder_right,inorder_right)

        return node