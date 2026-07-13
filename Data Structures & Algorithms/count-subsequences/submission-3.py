class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        
        def dfs(i, j): 
            if j == len(t): 
                memo[(i,j)] = 1
                return 1 
            if i == len(s):
                memo[(i,j)] = 1 
                return 0 
            if (i,j) in memo:
                return memo[(i,j)]
            take = 0 
            if s[i] == t[j]: 
                take = dfs(i+1, j+1) 
            dont = dfs(i+1, j)
            memo[(i,j)] = take + dont
            return take + dont
        
        return dfs(0, 0)
            
