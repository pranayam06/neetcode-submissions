class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows = len(matrix)
        cols = len(matrix[0]) 


        def is_valid(i, j, val): 
            return i < rows and j < cols and i >= 0 and j >= 0 and matrix[i][j] > val

        def dfs(i, j, prev): 
            if not is_valid(i, j, prev): 
                return 0
            if (i, j) in memo: 
                return memo[(i,j)]
            val = matrix[i][j] 
            m = 0
            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))
            memo[(i, j)] = res
            return res

        res = 0 
        for r in range(rows):
            for c in range(cols): 
                res = max(res, dfs(r,c,-1))

        return res 

                     
            
