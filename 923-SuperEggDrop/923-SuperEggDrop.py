# Last updated: 6/25/2026, 9:12:21 AM
class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        e=k
        f=n
        dp={}
        def dfs(e,f):
            if f==0 or f==1:
                return f
            
            if e==1:
                return f

            if (e,f) in dp:
                return dp[(e,f)]

            mn=float('inf')
            
            left=1
            right=f
            while left <=right:
                mid= (left+right)//2
                break_case = dfs(e - 1, mid - 1)     # egg breaks
                not_break_case = dfs(e, f - mid)     # egg survives
                temp= 1+max(break_case,not_break_case)
                mn= min(temp,mn)
                
                if break_case> not_break_case:
                    right=mid-1                
                else:
                    left=mid+1


            dp[(e,f)]=mn

            
            return mn
        
        return dfs(e,f)