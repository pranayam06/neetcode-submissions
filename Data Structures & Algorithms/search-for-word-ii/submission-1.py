class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode():
            def __init__(self): 
                self.arr = [None for _ in range(26)]
                self.eow = False
                self.word = ""
            
            def insert(self, word): 
                t = self
                for char in word: 
                    cur = t.arr

                    if not cur[ord(char) - ord('a')]: 
                        cur[ord(char) - ord('a')] = TrieNode()
                    t = cur[ord(char) - ord('a')]
                t.eow = True 
                t.word = word
        
        
        # initialize 

        trie = TrieNode()
        for word in words: 
            trie.insert(word)
        res = set()

        rows = len(board)
        cols = len(board[0])

        def is_valid(r, c, path): 
            return r < rows and c < cols and r >= 0 and c >= 0 and (r,c) not in path 
        
        def dfs(r, c, trie, path): 
            letter = board[r][c] 
            if not trie.arr[ord(letter) - ord('a')]:
                return False 
            path.add((r,c))

            new = trie.arr[ord(letter)- ord('a')] 
            if new.eow: 
                res.add(new.word)
            dirs = [(-1,0), (1,0),(0,1), (0,-1)]
            for (dx, dy) in dirs: 
                newr = r+ dx
                newc = c+dy
                if (is_valid(newr, newc, path)): 
                    dfs(newr, newc, new, path)
            path.remove((r,c))
            return True 
        path = set()

        for i in range(rows): 
            for j in range(cols): 
                dfs(i, j, trie, path)
                path.clear()
        return list(res)
                        











                    
