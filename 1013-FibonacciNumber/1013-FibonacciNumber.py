# Last updated: 6/25/2026, 9:12:12 AM
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        return self.fib_memo(n,memo)

    def fib_memo(self,n,memo):
        if n<=1:
            return n
        if n in memo:
            return memo[n]
        memo[n]=self.fib_memo(n-1,memo) + self.fib_memo(n-2,memo)
        return memo[n]