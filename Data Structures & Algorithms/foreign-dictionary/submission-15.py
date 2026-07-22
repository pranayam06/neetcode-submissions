class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # shorter word first 
        adjlist = defaultdict(list)
        all_chars = []  

        for word in words:
            for char in word: 
                all_chars.append(char)

        for i in range(len(words)-1): 
            first = words[i] 
            sec = words[i+1]
            ptr = 0
            while ptr < min(len(first), len(sec)):
                if first[ptr] == sec[ptr]: 
                    adjlist[first[ptr]]
                    ptr += 1 
                    if ptr == len(sec) and ptr < len(first):
                        return "" 
                else:
                    adjlist[sec[ptr]].append(first[ptr])
                    break
        path = set()
        visited = set()
        def dfs(c):   
            if c in visited: 
                return True 
            if c in path: 
                return False  
            
            path.add(c)
            for letter in adjlist[c]:
                if not dfs(letter):
                    return False 
            visited.add(c)
            res.append(c)
            return True 
        
        res = [] 
        
        for char in all_chars:
            if not dfs(char):
                return ""
            path.clear()

        return "".join(res)
                
                

