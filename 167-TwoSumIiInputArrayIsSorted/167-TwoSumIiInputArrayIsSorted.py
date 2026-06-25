# Last updated: 6/25/2026, 9:15:56 AM
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r=0,len(numbers)-1

        while l<r:
            if target-numbers[l]==numbers[r]:
                return [l+1,r+1]
            elif target-numbers[l]>numbers[r]:
                l+=1
            else:
                r-=1