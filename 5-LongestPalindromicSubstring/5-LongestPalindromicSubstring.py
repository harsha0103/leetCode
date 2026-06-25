# Last updated: 6/25/2026, 9:18:26 AM
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1=s
        s2=s[::-1]
        
        n=len(s)
        d=[[0]*(n+1) for i in range(n+1)]
        pal_len=0
        end_index=0
        for i in range(1,n+1):
            for j in range(1,n+1):

                if s1[i-1]==s2[j-1]:
                    d[i][j]= 1+d[i-1][j-1]
                    
                    if d[i][j]>pal_len:
                        index1=i-d[i][j]
                        index2=n-j
                        if index1==index2:
                            pal_len=d[i][j]
                            end_index=i



        return s[end_index-pal_len:end_index]

        
 