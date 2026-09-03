class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        
        dp = {}

        def is_valid(r,c): 
            return 0 <= r < ROWS and 0<=c < COLS and obstacleGrid[r][c] == 0
        
        if is_valid(0,0): dp[(0,0)]=1

        def dfs(r,c): 
            if (r,c) in dp: 
                return dp[(r,c)]
            
            res = 0 
            if is_valid(r, c-1): 
                res += dfs(r, c-1)
            if is_valid(r-1,c): 
                res += dfs(r-1, c)
            dp[(r,c)] = res 
            return res 
        
        return dfs(ROWS-1, COLS-1)
