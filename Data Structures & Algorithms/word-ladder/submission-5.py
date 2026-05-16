class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList: 
            return 0
        
        def is_valid(comp1, comp2):
            count = 0
            for i in range(len(comp1)): 
                if not comp1[i] == comp2[i]:
                    count+=1
            return (count == 1)
        
        q = deque()
        visited = [False for _ in range(len(wordList))]
        q.append(beginWord)

        def bfs():
            res = 1
            while q:
                length = len(q)
                for j in range(length):
                    cur = q.popleft() 
                    if cur == endWord:
                        return res

                    for i in range(len(wordList)):
                        if visited[i] == False and is_valid(wordList[i], cur): 
                            visited[i] = True
                            q.append(wordList[i])
                
                res+=1 
            return 0
        
        return bfs()


