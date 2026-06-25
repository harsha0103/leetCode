# Last updated: 6/25/2026, 9:09:50 AM
from collections import defaultdict
class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        graph={}

        for node in range(len(edges)):
            graph[node]=edges[node]

        visited=set()
        cache={}
        cycle_lengths=[]
           # Check each node for the longest cycle
        for node in graph:
            cycle_length = self.dfs_traverse(graph, {}, visited, node,cache)
            if cycle_length > 0:
                cycle_lengths.append(cycle_length)

        # Return the maximum cycle length or -1 if no cycle exists
        return max(cycle_lengths) if cycle_lengths else -1

    def dfs_traverse(self, graph, visiting, visited, node,cache):
        if node in visiting:
            # Cycle detected, calculate its length
            cache[node]=len(visiting)-visiting[node]
            return len(visiting)-visiting[node]

        if node in visited or node in cache:
            return 0

        visiting[node]=len(visiting)
        if graph[node] != -1:
            cycle_length = self.dfs_traverse(graph, visiting, visited, graph[node],cache)
            if cycle_length > 0:
                cache[node] = cycle_length

                return cycle_length

        visited.add(node)
        del visiting[node]
        cache[node]=0

        return 0
