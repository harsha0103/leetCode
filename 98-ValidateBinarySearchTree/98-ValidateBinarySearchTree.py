# Last updated: 6/25/2026, 9:16:48 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        visited=[]
        self.inorder(root,visited)
        return self.checkBST(visited)
    
    def inorder(self,root,visited):
        if not root:
            return 
        
        self.inorder(root.left,visited)
        visited.append(root.val)
        self.inorder(root.right,visited)
    
    def checkBST(self,visited):
        for i in range(1,len(visited)):
            if visited[i-1]>=visited[i]:
                return False
        return True