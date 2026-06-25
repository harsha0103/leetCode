# Last updated: 6/25/2026, 9:12:14 AM
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(1,len(words)):
            if not self.check_lexicograp(words[i-1],words[i],order):
                return False
        return True



    def check_lexicograp(self,current,next1,order):
        max_len= max(len(current),len(next1))

        for i in range(max_len):
            index1= order.index(current[i]) if i<len(current) else float('-inf')
            index2= order.index(next1[i]) if i<len(next1) else float('-inf')

            if index1<index2:
                return True
            if index2<index1:
                return False
        return True


