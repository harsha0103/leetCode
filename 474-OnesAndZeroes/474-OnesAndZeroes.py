# Last updated: 6/25/2026, 9:13:55 AM
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp={}

        def dfs(i,z,o):

            if z>m or o>n or i>=len(strs):
                return 0

            if (i,z,o) in dp:
                return dp[(i,z,o)]    
            take=0
            zeros=strs[i].count('0') 
            ones=strs[i].count('1')
            not_take=dfs(i+1,z,o)

            if zeros+z<=m and ones+o<=n:
                take=1+ dfs(i+1,zeros+z,ones+o)

            take=max(take,not_take)
            dp[(i,z,o)]=take
            return take
        
        return dfs(0,0,0)
            