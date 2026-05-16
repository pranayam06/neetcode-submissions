class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        cur = 0

        def is_valid(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] == 0:
                return False
            else:
                return True  

        def dfs(r, c):
            nonlocal cur
            cur+=1  
            grid[r][c] = 0
            deltar = [0, 0, 1, -1]
            deltac = [-1, 1, 0, 0]

            for i in range(4):
                if (is_valid(r+deltar[i], c+deltac[i])):
                    dfs(r+deltar[i], c+deltac[i]) 
        
        for row in range(ROWS):  
            for col in range(COLS):
                if grid[row][col] == 1: 
                    dfs(row, col)
                    res = max(cur, res) 
                    cur = 0
                    

        return res