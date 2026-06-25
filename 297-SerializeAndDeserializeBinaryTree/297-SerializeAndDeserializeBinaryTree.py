# Last updated: 6/25/2026, 9:14:34 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        def dfs(root):
            if not root:
                res.append('N')
                return 
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ','.join(res)
            

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr=data.split(',')
        arr.reverse()
        def dfs(arr):
            if not arr:
                return None
            
            val=arr.pop()
            if val=='N':
                return None 

            node=TreeNode(val)

            node.left=dfs(arr)
            node.right=dfs(arr)
            return node
        return dfs(arr)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))