# Last updated: 6/25/2026, 9:15:23 AM
class TrieNode(object):
    def __init__(self):
        self.child={}
        self.word=False

class Trie(object):

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word):
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
        curr=self.root
        for c in word:
            if c not in curr.child:
                return False
            curr=curr.child[c]
        return curr.word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr=self.root
        for c in prefix:
            if c not in curr.child:
                return False
            curr=curr.child[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)