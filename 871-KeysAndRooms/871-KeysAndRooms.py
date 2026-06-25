# Last updated: 6/25/2026, 9:12:31 AM
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited=self.dfs(rooms,0,set())
        if len (visited)==len(rooms):
            return True
        return False

    def dfs(self,rooms,node,visited):
        if node in visited:
            return 
        visited.add(node)

        for neighbors in rooms[node]:
            self.dfs(rooms,neighbors,visited)

        return visited 
        
        