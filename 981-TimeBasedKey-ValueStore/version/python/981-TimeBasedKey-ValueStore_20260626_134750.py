# Last updated: 6/26/2026, 1:47:50 PM
1from collections import defaultdict
2class TimeMap(object):
3
4    def __init__(self):
5        self.store=defaultdict(list)
6
7    def set(self, key, value, timestamp):
8        """
9        :type key: str
10        :type value: str
11        :type timestamp: int
12        :rtype: None
13        """
14        self.store[key].append([value,timestamp])
15        
16
17    def get(self, key, timestamp):
18        """
19        :type key: str
20        :type timestamp: int
21        :rtype: str
22        """
23        values=self.store[key]
24        l,r=0,len(values)-1
25        res=''
26        while l<=r:
27            mid=(l+r)//2
28
29            if values[mid][1]>timestamp:
30                r=mid-1
31            else:
32                res=values[mid][0]
33                l=mid+1
34        return res
35
36
37# Your TimeMap object will be instantiated and called as such:
38# obj = TimeMap()
39# obj.set(key,value,timestamp)
40# param_2 = obj.get(key,timestamp)