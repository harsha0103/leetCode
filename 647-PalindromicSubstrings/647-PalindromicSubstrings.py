# Last updated: 6/25/2026, 9:13:08 AM
class Solution:
    def countSubstrings(self, s):
        dp={}
        pal={}
        n=len(s)
        def is_pal(i,j):
            if i>=j :
                return True
            if (i, j) in pal:
                return pal[(i, j)]
            if s[i] != s[j]:
                pal[(i, j)] = False
            else:
                pal[(i, j)] = is_pal(i + 1, j - 1)
            return pal[(i, j)]
        
        def dfs(i):
            if i==len(s):
                return 0
            
            if i in dp:
                return dp[i]
            count=0
            for j in range(i,n): 
                if is_pal(i,j):
                    count+=1
            
            dp[i]=count+dfs(i+1)

            return dp[i]
        
        return dfs(0)


