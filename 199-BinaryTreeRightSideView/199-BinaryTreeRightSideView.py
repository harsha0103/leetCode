# Last updated: 6/25/2026, 9:15:30 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res =[]
        def dfs(root,depth):
            if not root:
                return None
            
            if depth>len(res):
                res.append(root.val)
            
            right=dfs(root.right,depth+1)
            left=dfs(root.left,depth+1)
 

        dfs(root,1)
        return res