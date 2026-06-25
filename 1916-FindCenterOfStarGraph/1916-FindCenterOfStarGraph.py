# Last updated: 6/25/2026, 9:10:08 AM
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        res=float()
        temp=0
        x,y=edges[0]
        res,temp=edges[1]

        if x==res or y==res:
            return res
        return temp