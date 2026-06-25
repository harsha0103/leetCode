# Last updated: 6/25/2026, 9:13:49 AM
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev = None  # Initialize prev as an instance variable
        self.res = float("inf")  # Initialize res as an instance variable

        def dfs(node):
            if not node:
                return

            # Left subtree
            dfs(node.left)

            # In-order traversal: Process current node
            if self.prev is not None:
                self.res = min(self.res, node.val - self.prev.val)
            self.prev = node  # Update prev

            # Right subtree
            dfs(node.right)

        dfs(root)
        return self.res