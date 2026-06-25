# Last updated: 6/25/2026, 9:10:11 AM
class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            rem = n%3
            if rem == 2 :
                return False
            n= n //3 
        return True 
