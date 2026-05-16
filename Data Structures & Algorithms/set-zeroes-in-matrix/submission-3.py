class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        top = False 

        # iterate through top 
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and matrix[r][c] == 0: 
                    top = True 
                elif matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix [r][0] = 0 
        print(matrix[0][0])
        for i in range(1, COLS):
            if matrix[0][i] == 0:
                for j in range(1, ROWS):
                    matrix[j][i] = 0

        for x in range(1, ROWS):
            if matrix[x][0] == 0:
                for y in range(1, COLS):
                    matrix[x][y] = 0
        print(matrix)
        if matrix[0][0] == 0: 
            for i in range(ROWS):
                matrix[i][0] = 0
        if top: 
            for i in range(COLS):
                matrix[0][i] = 0   