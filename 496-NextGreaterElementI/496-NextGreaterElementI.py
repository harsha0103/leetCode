# Last updated: 6/25/2026, 9:13:52 AM
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]

        for i in range(len(nums1)):
            nums=list(nums2)
            while len(nums)>0 and nums1[i]!=nums[0]:
                nums.pop(0)

            if len(nums)>0:
                nums.pop(0)
                while len(nums)>0 and nums[0]<nums1[i]:
                    nums.pop(0)
            if len(nums)>0:    
                    res.append(nums[0])
            else:
                    res.append(-1)

        return res




