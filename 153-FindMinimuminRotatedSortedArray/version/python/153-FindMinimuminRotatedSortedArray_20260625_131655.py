# Last updated: 6/25/2026, 1:16:55 PM
# do more
1class Solution(object):
2    def findMin(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        l,r=0,len(nums)-1
8        n=len(nums)
9        while l<=r:
10            if nums[l]<=nums[r]:
11                return nums[l]
12            
13            mid=(l+r)//2
14            prev= (mid-1+n)%n
15            nxt=(mid+1)%n
16
17            if nums[mid]<=nums[prev] and nums[mid]<=nums[nxt]:
18                return nums[mid]
19            
20            elif nums[mid]<nums[l]:
21                r=mid-1
22            else:
23                l=mid+1
24            
25