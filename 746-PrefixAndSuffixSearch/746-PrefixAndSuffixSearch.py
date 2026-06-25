# Last updated: 6/25/2026, 9:12:54 AM
class TreeNode:
    def __init__(self):
        self.child={}
        self.index=(False,-1)

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root=TreeNode()
        for ind in range(len(words)):
            self.insert(words[ind],ind)
        
    def insert(self,word,ind):
        curr=self.root
        for c in word:
            if c not in curr.child:
                curr.child[c]=TreeNode()
            curr=curr.child[c]
        curr.index=(True,ind)


    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        curr=self.root
        for c in pref:
            if c not in curr.child:
                return -1
            curr=curr.child[c]
        res =[]
        def dfs(curr,path):
            if curr.index[0] and path.endswith(suff):
                res.append(curr.index[1])
            for ch in curr.child:
                dfs(curr.child[ch],path+ch)
        
        dfs(curr,pref)
        return max(res) if res else -1





# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)