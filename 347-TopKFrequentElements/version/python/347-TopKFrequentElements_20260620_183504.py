# Last updated: 6/20/2026, 6:35:04 PM
# tok k
1from collections import defaultdict
2class Solution(object):
3    def topKFrequent(self, nums, k):
4        """
5        :type nums: List[int]
6        :type k: int
7        :rtype: List[int]
8        """
9        d=defaultdict(int)
10
11        for i in nums:
12            d[i]+=1
13        
14        res=[[] for _ in range(len(nums)+1)]
15
16        for key,value in d.items():
17            res[value].append(key)
18        
19        final=[]
20        while k>0:
21            if len(res[-1])==0:
22                res.pop()
23            else:
24                temp=res[-1].pop()
25                final.append(temp)
26                k-=1
27        return final
28        