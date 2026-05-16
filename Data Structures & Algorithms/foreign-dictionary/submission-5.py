class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        hmap = defaultdict(list)
        if len(words) == 1:
            return words[0]
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            if w1.startswith(w2) and len(w1) > len(w2):
                return ""  
            for j in range(min(len(w1), len(w2))):
                if not w1[j] == w2[j]:
                    hmap[w1[j]].append(w2[j])
                    break
        all_chars = set()
        for word in words:
            for ch in word:
                all_chars.add(ch)
    
        # now do top sort 
        self.res = ""
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                self.res = ""
                return False
            if node in visited:
                return True
            if node not in visited: 
                path.add(node)
                for nbor in hmap[node]:
                    if not dfs(nbor):
                        return False
                path.remove(node)
                visited.add(node)
                self.res = node + self.res
                return True

        for ch in all_chars:
            if not dfs(ch):
                return ""

        return self.res

            