class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        visited = set()
        
        q = deque()
        q.append(beginWord)
        ct = 0
        while q: 
            ct += 1
            for loop in range(len(q)): 
                word = q.popleft()
                if word == endWord: 
                    return ct 
                for i in range(len(word)): 
                    for j in range(ord('a'), ord('z') + 1):
                        if j == ord(word[i]):
                            continue
                        new_word = word[0:i] + chr(j) + word[i+1:]
                        if new_word not in visited and (new_word) in wordSet: 
                            q.append(new_word) 
                visited.add(word)
        
        return 0
            

                    


