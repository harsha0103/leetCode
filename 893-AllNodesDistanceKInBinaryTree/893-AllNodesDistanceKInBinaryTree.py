# Last updated: 6/25/2026, 9:12:27 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict,deque

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        ## convert the tree to undirected graph, so you can explore in birection 
        graph=defaultdict(list)
        def build_graph(node,parent ):

            if not node:
                return None
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)

            build_graph(node.left,node)
            build_graph(node.right,node)
        build_graph(root,None)


        q=deque([(target.val,0)])
        res=[]
        visited=set()
        while q:
            current,distance=q.popleft()
            if current in visited:
                continue
            visited.add(current)
            if distance==k:
                res.append(current) 
            elif distance < k:
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        q.append((neighbor,distance+1))
        
        return res