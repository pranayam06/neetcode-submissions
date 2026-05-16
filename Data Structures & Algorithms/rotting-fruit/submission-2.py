class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0]) 
        time = 0
        fresh = 0 
        q = deque() 
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1 
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        def is_valid(r, c):
            if r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == 1:
                return True
            return False

        while (q and fresh > 0):
            length = len(q)
            for fruit in range(length): 
                cur = q.popleft() 

                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]

                for i in range(4):
                    r = cur[0] + dr[i]
                    c = cur[1] + dc[i]

                    if is_valid(r, c) and visited[r][c] == False: 
                        fresh-=1
                        visited[r][c] = True 
                        grid[r][c] = 2
                        q.append([r,c])

            time += 1   
            
        
        if fresh == 0: 
            return time
        else:
            return -1

                


        