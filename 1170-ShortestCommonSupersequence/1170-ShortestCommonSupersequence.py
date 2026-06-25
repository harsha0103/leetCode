# Last updated: 6/25/2026, 9:11:41 AM
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        n,m=len(str1),len(str2)

        d=[['']*(m+1) for i in range(n+1) ]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    x=d[i-1][j-1]
                    d[i][j]=(x+str1[i-1])
                
                else:
                    if len(d[i-1][j])>len(d[i][j-1]):
                        d[i][j]=d[i-1][j]
                    else:
                        d[i][j]=d[i][j-1]
            
        scs=d[n][m]
        i,j=0,0
        res=''
        for c in scs:
            while i<n and c!=str1[i]:
                res+=str1[i]
                i+=1
            while j<m and c!=str2[j]:
                res+=str2[j]
                j+=1
            res+=c
            i+=1
            j+=1
        
        res=res+str1[i:]+str2[j:]
        return res
                

