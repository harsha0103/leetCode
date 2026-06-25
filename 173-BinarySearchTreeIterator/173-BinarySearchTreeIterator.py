# Last updated: 6/25/2026, 9:15:52 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.visited=[]
        self.inorder(root)


    
    def inorder(self,root):
        if not root:
            return 
        
        self.inorder(root.right)
        self.visited.append(root.val)
        self.inorder(root.left)

    def next(self):
        """
        :rtype: int
        """
        res=self.visited.pop()
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.visited)>0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()