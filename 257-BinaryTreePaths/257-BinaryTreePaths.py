# Last updated: 6/25/2026, 9:14:53 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        q=[(root,str(root.val))] if root else None
    
        res=[]

        while q:
            curr,curr_str=q.pop()

            if not curr.left and not curr.right:
                res.append(curr_str)
            
            if curr.left:
                q.append((curr.left,curr_str+'->'+str(curr.left.val)))
            
            if curr.right:
                q.append((curr.right,curr_str+'->'+str(curr.right.val)))
        
        return res
            
