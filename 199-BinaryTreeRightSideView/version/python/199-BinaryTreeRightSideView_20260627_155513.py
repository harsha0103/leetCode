# Last updated: 6/27/2026, 3:55:13 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def rightSideView(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: List[int]
12        """
13        res =[]
14        def dfs(root,depth):
15            if not root:
16                return None
17            
18            if depth>len(res):
19                res.append(root.val)
20            
21            right=dfs(root.right,depth+1)
22            left=dfs(root.left,depth+1)
23 
24
25        dfs(root,1)
26        return res