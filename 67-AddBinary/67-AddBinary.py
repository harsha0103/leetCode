# Last updated: 6/25/2026, 9:17:12 AM
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry=0
        res=''
        a,b=a[::-1],b[::-1]

        for i in range(max(len(a),len(b))):
            digitA =int(a[i]) if i<len(a) else 0
            digitB =int(b[i]) if i<len(b) else 0
            
            print(digitA,digitB)
            total=digitA + digitB + carry
            char= str(total%2)

            carry = 1 if total>1 else 0

            res = char+res
        if carry ==1:
            res= "1"+res
        return res
       



        
        
            
            