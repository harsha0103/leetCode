# Last updated: 6/25/2026, 9:14:11 AM
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #O(M*N)
        '''
        j=0
        for i in ransomNote:
            if (i in magazine):
                magazine=magazine.replace(i,'',1)
                ransomNote=ransomNote.replace(i,'',1)
        if (ransomNote):
            return False
        else:
            return True'''
        
        #using hashmap 

        '''magCount= {Char:magazine.count(Char) for Char in magazine }''' # O(M*M)
        magCount={}
        for i in magazine:
            if i in magCount:
                magCount[i] +=1
            else:
                magCount[i]=1

        print(magCount)
        
        for i in ransomNote:
            if (i in magCount) and magCount[i]>0:
                magCount[i]-=1
            else:
                return False
        return True
    
  