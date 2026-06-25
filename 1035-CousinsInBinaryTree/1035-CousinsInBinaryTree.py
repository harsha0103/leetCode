# Last updated: 6/25/2026, 9:12:05 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        stack=[(root,[root.val])] if root else []
        prevx=[]
        prevy=[]

        while stack:
            current,lis=stack.pop()
            if current.val==x:
                prevx=lis
            if current.val==y:
                prevy=lis
            if current.left:
                stack.append((current.left,lis+[current.left.val]))
            if current.right:
                stack.append((current.right,lis+[current.right.val]))
        print(prevx,prevy)
        if len(prevx) == len(prevy):
            if prevx[-2]!=prevy[-2]:
                return True 

        return False

            

        