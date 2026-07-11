class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        visited = set()
        adjlist = defaultdict(list)
        wordList.append(beginWord)

        if endWord not in wordList: 
            return 0

        for word in wordList: 
            for i in range(len(word)): 
                for j in range(ord('a'), ord('z') + 1):
                    if j == ord(word[i]):
                            continue
                    new_word = word[0:i] + chr(j) + word[i+1:]
                    if (new_word) in wordSet: 
                        adjlist[word].append(new_word) 
        
        q = deque()
        q.append(beginWord)
        ct = 0
        while q: 
            ct += 1
            for loop in range(len(q)): 
                word = q.popleft() 
                visited.add(word)

                if word == endWord: 
                    return ct 
                for new_word in adjlist[word]:
                    if new_word not in visited: 
                        q.append(new_word) 
        
        return 0
            

                    


