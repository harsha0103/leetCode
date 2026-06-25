# Last updated: 6/25/2026, 9:18:17 AM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #return ("".join(reversed(str(x)))==str(x))
        if x<0:
            return False

        initial=x
        final=0
        while x>0:
            final= final*10+(x%10)
            x=x//10 

        if(initial==final):
            return True
        else:
            return False

