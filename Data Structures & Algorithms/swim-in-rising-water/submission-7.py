class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        minheap = [] # (time till now, r, c)

        hmap = dict()
        heapq.heappush(minheap, (grid[0][0], 0, 0))
        hmap[(0,0)] = grid[0][0]

        while (minheap): 
            (minmax, r, c) = heapq.heappop(minheap) 

            dirs = [(0,1), (1,0), (-1,0), (0,-1)]
            for dx, dy in dirs: 
                new_r = r + dx
                new_c = c + dy 
                if not (0<=new_r< len(grid) and 0<=new_c<len(grid[0])): 
                    continue
                if (new_r, new_c) in hmap and hmap[(new_r, new_c)] <= max(grid[new_r][new_c], minmax):
                    continue
                hmap[(new_r, new_c)] = max(grid[new_r][new_c], minmax) 
                heapq.heappush(minheap, (hmap[(new_r, new_c)], new_r, new_c))
        print()
        return hmap[(len(grid) -1, len(grid[0]) -1)]
        
            




