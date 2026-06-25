# Last updated: 6/25/2026, 9:15:07 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        visited=[]
        self.inorder(root,visited)
        return visited[k-1]
        
    
    def inorder(self,root,visited):
        if not root:
            return None
        
        self.inorder(root.left,visited)
        visited.append(root.val)
        self.inorder(root.right,visited)
