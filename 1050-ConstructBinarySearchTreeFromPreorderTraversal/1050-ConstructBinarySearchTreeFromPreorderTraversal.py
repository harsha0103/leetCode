# Last updated: 6/25/2026, 9:12:01 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder)==0:
            return None
        val=preorder[0]
        node=TreeNode(val)
        index=len(preorder)
        for i in range(1,len(preorder)):
            if val<preorder[i]:
                index=i
                break
        
        node.left=self.bstFromPreorder(preorder[1:index])
        node.right=self.bstFromPreorder(preorder[index:])
        return node
