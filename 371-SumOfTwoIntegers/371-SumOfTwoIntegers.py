# Last updated: 6/25/2026, 9:14:13 AM
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK=0XFFFFFFFF
        MAX=0X7FFFFFFF

        for i in range(32):
            xor=(a^b)& MASK
            annd= ((a&b) <<1)& MASK
            a=xor
            b=annd
            
        return a if a<MAX else ~(a^MASK)