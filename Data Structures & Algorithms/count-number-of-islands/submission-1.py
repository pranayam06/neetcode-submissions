class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        def is_valid(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] == "0":
                return False
            else:
                return True  

        def dfs(r, c):  
            # pre: r and c are valid 
            grid[r][c] = "0"
            #find where to turn grid val to 0
            deltar = [0, 0, 1, -1]
            deltac = [-1, 1, 0, 0]

            for i in range(4):
                if (is_valid(r+deltar[i], c+deltac[i])):
                    dfs(r+deltar[i], c+deltac[i])
        
        for row in range(ROWS):  
            for col in range(COLS):
                if grid[row][col] == "1":
                    res += 1 
                    dfs(row, col)
                    

        return res