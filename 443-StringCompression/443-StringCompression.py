# Last updated: 6/25/2026, 9:14:00 AM
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars.append('!')
        res=''
        i=0
        j=1

        while j<len(chars):
            if chars[i]!=chars[j]:
                if (j-i)>1:
                    res=res+chars[i]+str(j-i)
                else:
                    res+=chars[i]

                i=j
            j+=1
        for i in range(len(res)):
            chars[i]=res[i]
        return len(res)
