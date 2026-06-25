# Last updated: 6/25/2026, 9:17:38 AM
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n,m=len(num1),len(num2)
        res=[0]*(n+m)

        num1=num1[::-1]
        num2=num2[::-1]
        
        for i in range(n):
            for j in range(m):
                temp=(ord(num1[i])-ord('0'))* (ord(num2[j])-ord('0'))
                temp+=res[i+j]
                res[i+j+1]+=temp//10
                res[i+j]=temp%10
        
        res.reverse()
        for i in range(len(res)):
            if res[i]!=0:
                break
    

        temp=''.join(str(r) for r in res[i:])
        return temp