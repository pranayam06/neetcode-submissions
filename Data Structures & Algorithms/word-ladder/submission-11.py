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
        
        front = deque()
        front.append(beginWord)
        back = deque()
        back.append(endWord)

        ct = 1
        while front and back: 
            if len(front) > len(back):
                front, back = back, front
            
            for i in range(len(front)):
                word = front.popleft()
                visited.add(word)
                for nbor in adjlist[word]:
                    if nbor in back:
                        return ct + 1
                    else:
                        if not nbor in visited:
                            front.append(nbor) 
            ct += 1
            
        return 0
            

                    


