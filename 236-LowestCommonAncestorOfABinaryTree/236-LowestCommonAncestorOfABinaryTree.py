# Last updated: 6/25/2026, 9:15:00 AM
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
        
        p_arr=self.dfs(root,p)
        q_arr=self.dfs(root,q)
        res=0
        while p_arr and q_arr:
            curr_p,curr_q=p_arr.pop(),q_arr.pop()
            if curr_p!=curr_q:
                break
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
        
        return []
        