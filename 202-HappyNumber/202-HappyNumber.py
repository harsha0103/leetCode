# Last updated: 6/25/2026, 9:15:28 AM
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        check=set()

        def mul(num):
            res=0
            while num:
                temp=num%10
                res+=temp*temp
                num=num//10
            return res

        while n not in check:
            check.add(n)
            n=mul(n)
            if n==1:
                return True
            
        return False
