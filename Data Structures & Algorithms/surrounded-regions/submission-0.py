class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        visitedO = set()

        ROWS = len(board)
        COLS = len(board[0])

        def is_valid(r,c): 
            # not border and unvisited 
            if r > 0 and r < ROWS-1 and c > 0 and c < COLS-1 and board[r][c] == "O": 
                return True
            return False

        def dfs(r, c):
            if tuple([r,c]) in visited or board[r][c] == "X": 
                return 
            # assert: is_valid(r,c)
            visited.add(tuple([r,c]))
            if board[r][c] == "O":
                visitedO.add(tuple([r,c]))
            
            deltar = [-1, 1, 0, 0]
            deltac = [0, 0, -1, 1]

            for i in range(4):
                new_r = r + deltar[i]
                new_c = c + deltac[i]

                if (is_valid(new_r, new_c)):
                    dfs(new_r, new_c) 

        #top and bottom 
        for x in range(COLS): 
            dfs(0, x)
            dfs(ROWS-1, x)

        for y in range(1, ROWS-1):
            dfs(y,0)
            dfs(y, COLS-1)
        print(visitedO)
        # completed visited Os  
        for j in range(ROWS):
            for k in range(COLS):
                if board[j][k]== "O" and tuple([j,k]) not in visitedO:
                    board[j][k]= "X"



        
        
        

