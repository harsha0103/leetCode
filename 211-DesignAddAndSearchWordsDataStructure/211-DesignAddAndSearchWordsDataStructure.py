# Last updated: 6/25/2026, 9:15:20 AM
class TrieNode(object):
    def __init__(self):
        self.child={}
        self.word=False

class WordDictionary(object):

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr=self.root
        for c in word:
            if c not in curr.child:
                curr.child[c]=TrieNode()
            curr=curr.child[c]
        curr.word=True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(i,curr):
            for c in range(i,len(word)):
                char=word[c]
                if char!='.':
                    if char not in curr.child:
                        return False
                    
                    curr=curr.child[char]
                
                else:
                    for new_c in curr.child.values():
                        if dfs(c+1,new_c):
                            return True
                    return False
            return curr.word


        return dfs(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)