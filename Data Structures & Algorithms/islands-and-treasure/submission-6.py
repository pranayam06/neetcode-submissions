from collections import deque 

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # "nearest" -- implies BFS just because we want to for every node find the nearest treasure chest 
        # take the opposite so start at the treasure chest and go to all the land cells that CAN be reached and CAN be traversed 

        # must iterate once and find all the treasure chests to start at 
        ROWS = len(grid)
        COLS = len(grid[0])

        chests = []
        # hehe find all chests here
        for i in range(ROWS): 
            for j in range(COLS): 
                if grid[i][j] == 0: 
                    chests.append((i, j))
        # inf is not seen yet 
    

        q = deque(chests)
        def is_valid(r, c): 
            return 0 <= r < ROWS and 0 <= c < COLS 

        depth = 0
        seen = set()
       
        while(q): 

            for _ in range(len(q)): 
                (r,c) = q.popleft()
                if grid[r][c] != 0:
                    grid[r][c] = depth 
                dirs = [(-1,0), (1,0), (0,1), (0,-1)]
                for dx, dy in dirs: 
                    newr = dy + r 
                    newc = dx + c 
                    
                    if (is_valid(newr, newc)) and grid[newr][newc] == 2147483647 and (newr, newc) not in seen:
                        q.append((newr,newc)) 
                        seen.add((newr,newc))
            
            depth += 1
        
        

                


















