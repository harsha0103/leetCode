# Last updated: 6/25/2026, 9:11:28 AM
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        return self.fib_memo(n,memo)
        
    def fib_memo(self,n,memo):
        if n<=0:
            return 0
        if n==1:
            return 1
        if n in memo:
            return memo[n]
        
        memo[n]= self.fib_memo(n-1,memo)+ self.fib_memo(n-2,memo)+self.fib_memo(n-3,memo)
        return memo[n]