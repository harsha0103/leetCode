# Last updated: 6/25/2026, 9:16:25 AM
from collections import deque,defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        neighbor=defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+'*'+word[j+1:]
                neighbor[pattern].append(word)
        
        q=deque([(beginWord,1)])
        visited=set([beginWord])

        while q:
            curr_word,dist=q.popleft()
            if curr_word==endWord:
                return dist
            
            for j in range(len(curr_word)):
                pattern=curr_word[:j]+'*'+curr_word[j+1:]
                for word in neighbor[pattern]:
                    if word not in visited:
                        visited.add(word)
                        q.append((word,dist+1))
        return 0
        