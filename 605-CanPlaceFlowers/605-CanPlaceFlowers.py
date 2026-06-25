# Last updated: 6/25/2026, 9:13:20 AM
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count=0
        flowerbed =[0]+flowerbed+[0]
        for i in range(1,len(flowerbed)-1):
            
            if(flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0):
                count+=1
                flowerbed[i]=1

        return count>=n
            
