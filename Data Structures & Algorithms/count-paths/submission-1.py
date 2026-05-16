class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        memo[0][0] = 1
        def dfs(r, c):
            if r == 0 and c == 0:
                return 1
            if c == 0:
                l = 0
            elif memo[r][c-1] > -1:
                l = memo[r][c-1]
            else:
                l = dfs(r, c-1)

            if r == 0:
                u = 0
            elif memo[r-1][c] > -1:
                u = memo[r-1][c]
            else:
                u = dfs(r-1, c)
            
            memo[r][c] = l + u
            return l+u
        
        dfs(m-1, n-1) 
        return memo[-1][-1]

                

