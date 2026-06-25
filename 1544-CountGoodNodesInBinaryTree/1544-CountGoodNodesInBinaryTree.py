# Last updated: 6/25/2026, 9:10:46 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count=[0]
        def dfs(root,max_val):
            if not root:
                return 
            
            count[0]= 1+count[0] if root.val>=max_val else count[0]

            max_val=max(max_val,root.val) 
        
            left=dfs(root.left,max_val)
            right=dfs(root.right,max_val)
            return 
        
        dfs(root,float('-inf'))
        return count[0]