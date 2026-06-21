class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo: 
                return memo[(i, j)]
            if i == len(word1):
                return abs(len(word2)-j)
            if j == len(word2):
                return abs(len(word1)-i)
            if i > len(word1) or j > len(word2): 
                return max(len(word1),len(word2))
            if word1[i] == word2[j]: 
                memo[(i, j)] = dfs(i+1, j+1)
                return memo[(i, j)] 
            else: 
                replace = dfs(i+1, j+1) + 1
                insert = dfs(i, j+1) +1
                delete = dfs(i+1, j) + 1
                memo[(i, j)] = min(replace, insert, delete)
                return memo[(i, j)] 
        
        return dfs(0, 0)
            


            
