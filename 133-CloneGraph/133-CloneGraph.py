# Last updated: 6/25/2026, 9:16:17 AM
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldtonew={}

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]
            if not node:
                return None 
            node1=Node(node.val)
            oldtonew[node]=node1
            for nei in node.neighbors:
                node1.neighbors.append(dfs(nei))
            
            return node1
        return dfs(node)