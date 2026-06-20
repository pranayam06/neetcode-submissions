class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        # dp[text2] [text1]

        def dfs(x, y): 
            if (x,y) in memo: 
                return memo[(x,y)]
            if x < 0 or y < 0: 
                return 0
            if text1[x] == text2[y]: 
                memo[(x,y)] = 1 + dfs(x-1, y-1)
            else: 
                memo[(x,y)] = max(dfs(x, y-1), dfs(x-1, y), dfs(x-1,y-1))                
            return memo[(x,y)]

        return dfs(len(text1)-1, len(text2)-1)