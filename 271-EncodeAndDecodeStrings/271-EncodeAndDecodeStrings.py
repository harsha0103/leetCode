# Last updated: 6/25/2026, 9:14:45 AM
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res=[]
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return ''.join(res)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        arr=[]
        i=0
        while i < len(s):
            j=i
            while s[j]!='#':
                j+=1
            num=int(s[i:j])
            j+=1

            new_str=s[j:j+num]
            arr.append(new_str)
            i=j+num
        return arr
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))