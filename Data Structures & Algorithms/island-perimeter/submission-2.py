class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        adjlist = defaultdict(list)

        def check(r,c): 
            ct = 0 
            dirs = ((-1,0), (1,0), (0,1), (0,-1))
            for dx, dy in dirs: 
                i = r + dy 
                j = c + dx
                if (i) < 0 or ROWS <= (i) or COLS <= (j) or j < 0 or grid[i][j] == 0: 
                    ct += 1
            return ct   

        res = 0
        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == 1: 
                    res += check(r,c)
        return res
                    
        

                 
        
