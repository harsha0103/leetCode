# Last updated: 6/25/2026, 9:14:58 AM
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l,r=0,0
        res=[]
        q=deque()
        while r <len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)    
            if q[0]<l:
                q.popleft()
            
            if r+1>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1

            
        return res


                


        