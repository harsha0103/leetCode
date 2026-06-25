# Last updated: 6/25/2026, 9:15:03 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        arr_p=self.dfs(root,p)
        arr_q=self.dfs(root,q)
        res=None
        while arr_p and arr_q:
            curr_p,curr_q=arr_p.pop(),arr_q.pop()
            if curr_p!=curr_q:
                return res
            res=curr_p
        return res
    
    def dfs(self,root,p):
        if not root:
            return None
        
        if root==p:
            return [root]
        
        left=self.dfs(root.left,p)
        if left:
            left.append(root)
            return left
        right=self.dfs(root.right,p)
        if right:
            right.append(root)
            return right
        