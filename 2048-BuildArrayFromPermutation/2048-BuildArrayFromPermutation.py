# Last updated: 6/25/2026, 9:10:00 AM
class Solution(object):
    def buildArray(self, nums):
        results = [0] * len(nums) 
        results1= []
        for i in range(len(nums)):
            #if (len(nums)>nums[i] and nums[i]>=0):
                results[i]=nums[nums[i]]
                results1.append(nums[nums[i]])

        #return results1
        return [nums[i] for i in nums]

                
        