class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)] 
        dp[0][0] = 1

        def is_valid(x, y): 
            return x < n and x >= 0 and y < m and y >= 0  

        def dfs(x, y):  
            if dp[x][y] > 0:
                return dp[x][y] 
            else: 
                if is_valid(x-1, y): 
                    dp[x][y] += dfs(x-1,y)
                if is_valid(x, y-1): 
                    dp[x][y] += dfs(x,y-1)
                return dp[x][y]
        
        dfs(n-1, m-1)
        return dp[n-1][m-1]

            
