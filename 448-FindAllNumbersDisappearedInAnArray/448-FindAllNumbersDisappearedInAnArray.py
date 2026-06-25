# Last updated: 6/25/2026, 9:13:58 AM
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set_nums= set(nums)
        #result=[]
        j=0

        for i in range(1,len(nums)+1):
            if not(i in set_nums):
                nums[j]=i
                j+=1
        return nums[:j]