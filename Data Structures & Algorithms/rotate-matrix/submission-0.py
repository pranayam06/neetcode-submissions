class Solution:
    def rotate(self, matrix: List[List[int]]) -> None: 
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        l, r = 0, len(matrix) - 1
        while l < r: 
            for i in range(r-l):
                top, bot = l, r

                topleft = matrix[top][l+i]

                matrix[top][l+i] = matrix[bot-i][l]

                matrix[bot-i][l] = matrix[bot][r-i]

                matrix[bot][r-i] = matrix[top+i][r]

                matrix[top+i][r] = topleft 
            l += 1 
            r-=1
        
        