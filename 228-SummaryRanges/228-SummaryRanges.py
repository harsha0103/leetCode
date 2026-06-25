# Last updated: 6/25/2026, 9:15:09 AM
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if (len(nums)==1):
            return [str(nums[0])]
        o=[]
        start =-1.5
        end = -1.5
        for i,j in enumerate(nums):
            if ((i+1)<len(nums) and (j+1)==(nums[i+1])):
                if (start==-1.5):
                    start=j
                continue
            else:
                end=j
            
            if(end !=-1.5 and start==-1.5):
                o.append(str(end))
                end=-1
            elif(end !=-1.5 and start!=-1.5):
                o.append(str(start) + "->" + str(j))
                end,start=-1.5,-1.5
        return o
