# Last updated: 6/25/2026, 9:10:55 AM
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=sorted(nums)
        print(temp)
        d= {}
        for i in range(len(temp)): 
            if temp[i] not in d:
                d[temp[i]]=i
        res=[]

        for i in range(len(nums)):
            res.append(d[nums[i]])

        return res