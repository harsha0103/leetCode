# Last updated: 6/25/2026, 9:18:24 AM
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 :
            return s
        
        rows=['']*min(numRows,len(s))
        down= True
        j=0
        for i in s:
            if down:
                rows[j]+=i 
                j+=1
            else:
                rows[j]+=i
                j-=1

            if j==numRows-1:
                down=False
            elif j==0:
                down=True               
        return "".join(rows)

        
        