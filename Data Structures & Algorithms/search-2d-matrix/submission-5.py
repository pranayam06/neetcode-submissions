class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0 
        r = ROWS * COLS -1
        m = 0
        while (l <= r):  
            m = l + ((r - l)//2) 

            row = int(m//COLS)
            col = int(m%COLS)
            val = matrix[row][col]

            if val == target: 
                return True 
            elif val < target: 
                l = m + 1
            else: 
                r = m-1
        
        return False


            

        

        