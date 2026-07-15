class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = {}

        TARGET = (ROWS-1, COLS-1)

        def is_valid(i,j): 
            return (0 <= i < ROWS and 0 <= j < COLS)
        
        res = 1000000

        def dfs(i, j): 
            if (i,j) == TARGET: 
                dp[(i,j)] = grid[i][j]
                return grid[i][j] 
            if (i,j) in dp: 
                return dp[(i,j)]
            directions = [(1,0), (0,1)]
            min_path = 10000000
            for dx, dy in directions: 
                new_row = i + dx 
                new_col = j + dy 

                if is_valid(new_row, new_col): 
                    min_path = min(dfs(new_row, new_col), min_path)
            dp[(i,j)] = grid[i][j] + min_path
            return grid[i][j] + min_path

        return dfs(0,0)

