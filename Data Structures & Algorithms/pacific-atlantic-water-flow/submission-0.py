class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0]) 
        atlantic = set()
        pacific = set()
        pacvisited = set()
        atlvisited = set()


        def is_valid(atl, r, c):
            if r >= 0 and r < ROWS and c >= 0 and c < COLS and tuple([r,c]):
                if(atl):
                    if tuple([r,c]) in atlvisited:
                        return False 
                else:
                    if tuple([r,c]) in pacvisited:
                        return False 
                
                return True

            else: 
                return False


        def dfs(atl, r, c, last_val): 
            cur_val = heights[r][c]
            if (cur_val >= last_val):  

                if (atl):  
                    atlantic.add(tuple([r,c]))
                    atlvisited.add(tuple([r,c]))
                else:  
                    # assert is pacific
                    pacific.add(tuple([r,c]))
                    pacvisited.add(tuple([r,c]))
                deltar = [1, -1, 0, 0]
                deltac = [0, 0, -1, 1] 

                for i in range(4):
                    if is_valid(atl, r + deltar[i], c+deltac[i]): 

                        dfs(atl, r + deltar[i], c+ deltac[i], cur_val)
        
        # top and bottom
        for x in range(COLS):
            dfs(True, ROWS-1, x, -1)
            dfs(False, 0, x, -1)
        
        # left and right
        for y in range(ROWS-1):
            dfs(True, y, COLS-1, -1)
            dfs(False, ROWS-1-y, 0, -1)
        
        res = []  
        print(pacific)
        print(atlantic)

        for r,c in pacific: 
            if tuple([r,c]) in atlantic:
                res.append([r,c])
        
        return res


        






