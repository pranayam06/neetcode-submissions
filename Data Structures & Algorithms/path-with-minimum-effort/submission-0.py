class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])

        def is_valid(r, c): 
            return r<ROWS and r >= 0 and c < COLS and c>=0
        
        seen = set()
        heap = [(0, (0, 0))]
        while(heap): 
            cost, (r,c) = heapq.heappop(heap)
            if (r,c) == (ROWS-1,COLS-1): 
                return cost 
            
            if (r, c) in seen: 
                continue
            seen.add((r,c))

            h = heights[r][c]    
            dirs = [(-1,0), (1,0), (0,-1), (0,1)] 
            for dx, dy in dirs: 
                x = r + dx
                y = c + dy
                if is_valid(x,y):
                    heapq.heappush(heap, (max(abs(heights[x][y] - h), cost), (x, y))) 
            
        
                    





                

        