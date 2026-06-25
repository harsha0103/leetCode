# Last updated: 6/25/2026, 9:18:23 AM
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        rev=0
        neg=1
        if x<0:
            neg=-1

        while abs(x)>0:
            rev=rev *10+ abs(x)%10
            x=abs(x)//10
        
        if (rev*neg> -2**31 and rev*neg<2**31-1):
            return rev*neg
        else:
            return 0

