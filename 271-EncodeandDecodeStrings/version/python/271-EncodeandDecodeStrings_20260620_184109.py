# Last updated: 6/20/2026, 6:41:09 PM
1class Codec:
2
3    def encode(self, strs):
4        """Encodes a list of strings to a single string.
5        
6        :type strs: List[str]
7        :rtype: str
8        """
9        res=[]
10        for s in strs:
11            res.append(str(len(s)))
12            res.append("#")
13            res.append(s)
14        return ''.join(res)
15
16    def decode(self, s):
17        """Decodes a single string to a list of strings.
18        
19        :type s: str
20        :rtype: List[str]
21        """
22        arr=[]
23        i=0
24        while i < len(s):
25            j=i
26            while s[j]!='#':
27                j+=1
28            num=int(s[i:j])
29            j+=1
30
31            new_str=s[j:j+num]
32            arr.append(new_str)
33            i=j+num
34        return arr
35        
36
37# Your Codec object will be instantiated and called as such:
38# codec = Codec()
39# codec.decode(codec.encode(strs))