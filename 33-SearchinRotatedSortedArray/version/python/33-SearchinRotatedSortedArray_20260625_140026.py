# Last updated: 6/25/2026, 2:00:26 PM
# this is easier than finding the min in rotated array
1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        l,r=0,len(nums)-1
9        
10        while l<=r:
11            mid=(l+r)//2
12            if nums[mid]==target:
13                return mid
14            elif nums[mid]>=nums[l]:
15                if target>=nums[l] and target<nums[mid]:
16                    r=mid-1
17                else:
18                    l=mid+1
19            
20            else:
21                if target<=nums[r] and target>nums[mid]:
22                    l=mid+1
23                else:
24                    r=mid-1
25            
26        return -1
27