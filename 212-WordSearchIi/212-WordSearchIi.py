# Last updated: 6/25/2026, 9:15:18 AM
class TrieNode(object):
    def __init__(self):
        self.child={}
        self.word=None
    
    def addWord(self,word):
        curr=self
        for c in word:
            if c not in curr.child:
                curr.child[c]=TrieNode()
            curr=curr.child[c]
        curr.word=word


class Solution(object):
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root=TrieNode()
        for word in words:
            root.addWord(word)
        
        row,col=len(board),len(board[0])
        res,visited=set(),set()
        def dfs(i,j,root):
            r_valid= 0<= i<row
            c_valid= 0<= j<col

            if (not r_valid or not c_valid or (i,j) in visited or board[i][j] not in root.child):
                return 
            
            visited.add((i,j))
            root=root.child[board[i][j]]
            if root.word:
                res.add(root.word)
                root.word=None 
            
            dfs(i+1,j,root)
            dfs(i,j+1,root)
            dfs(i,j-1,root)
            dfs(i-1,j,root)
            visited.remove((i,j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,root)
        res= list(res)
        return res
