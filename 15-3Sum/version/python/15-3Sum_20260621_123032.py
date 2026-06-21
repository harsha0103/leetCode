# Last updated: 6/21/2026, 12:30:32 PM
# three pointer with O(n2) time and O(1) space excluding the result array
1class Solution(object):
2    def threeSum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7        nums.sort()
8        res=[]
9        for i in range(len(nums)):
10            l,r=i+1,len(nums)-1
11            
12            if i>0 and nums[i]==nums[i-1]:
13                i+=1
14                continue
15
16            while l<r:
17                if nums[i]+nums[l]+nums[r]==0:
18                    res.append([nums[i],nums[l],nums[r]])
19                    l+=1
20                    r-=1
21                    while l<r and nums[l]==nums[l-1]:
22                        l+=1
23                elif nums[i]+nums[l]+nums[r]>0:
24                    r-=1
25                else:
26                    l+=1
27        return res
28            