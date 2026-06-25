# Last updated: 6/25/2026, 9:11:54 AM
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # Step 2: Target is to find the closest we can get to half of the total
        # because two equal subsets give minimum difference
        m=sum(stones)//2
        n=len(stones)

        d=[[False] * (m+1) for i in range(n+1)]
        
        d[0][0]=True
        for i in range(1,n+1):
            for j in range(m+1):
                if j ==0:
                    d[i][j]= True
                
                if stones[i-1]>j:
                    # Current stone is too big to be included in current sum

                    d[i][j]=d[i-1][j]
                
                else:
                    d[i][j]=d[i-1][j] or d[i-1][j-stones[i-1]]
        
        subset1=0
        # Step 6: Find the largest sum j (<= total//2) that we can form
        # This becomes our first subset sum (subset1)
        for j in range(m+1):
            if d[n][j]:
                subset1=j
      
        # Step 7: The other subset will be (total - subset1)
        # Difference between them: abs(subset1 - (total - subset1)) = abs(2*subset1 - total)


        return abs(2*subset1 - sum(stones))