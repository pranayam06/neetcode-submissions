class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        dist = 1 
        tbd = 0  
        q = collections.deque()
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    tbd += 1
                elif grid[r][c] == 0:
                    q.append([r,c]) 
                    visited[r][c] = True    
        
        def is_valid(r, c):
            if r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == INF:
                return True 
            return False

        #bfs search 
        while (q): 
            length = len(q) 
            print(dist)

            for node in range(length):
                cur = q.popleft() 
                
                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]

                for i in range(4):
                    r = cur[0] + dr[i]
                    c = cur[1] + dc[i]

                    if is_valid(r,c) and not visited[r][c]:
                        visited[r][c] = True
                        grid[r][c] = dist   
                        tbd -= 1
                        q.append([r,c])  

            dist += 1




                    