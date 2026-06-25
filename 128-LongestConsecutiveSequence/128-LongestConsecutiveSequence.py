# Last updated: 6/25/2026, 9:16:23 AM
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest=0
        num_set=set(nums)
        done=set()
        for n in nums:
            if n-1 not in num_set and n not in done:
                done.add(n)
                temp=1
                while n+1 in num_set:
                    temp+=1
                    n+=1
                longest=max(longest,temp)
            
        return longest 
        