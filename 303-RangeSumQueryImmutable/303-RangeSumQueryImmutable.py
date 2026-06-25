# Last updated: 6/25/2026, 9:14:32 AM
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix=[0]*(len(nums)+1)
        total=0
        for i in range(len(nums)+1):
            self.prefix[i]=total
            if i<len(nums):
                total+=nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right+1]-self.prefix[left]
    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)