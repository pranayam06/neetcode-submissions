class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        n = len(word1)
        m = len(word2)

        def dfs(i, j):
            if (i == len(word1)):
                return len(word2)-j
            if (j == len(word2)):
                return len(word1) - i
            if (i,j) in dp:
                return dp[(i,j)] 
            # assert j < len(word2)
            elif (i < len(word1) and word1[i] == word2[j]):
                dp[(i, j)] = dfs(i + 1, j + 1) 
            else: 
                opts = [dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1)]
                dp[(i, j)] = min(opts) +1
            return dp[(i,j)]
            
        return dfs(0,0)