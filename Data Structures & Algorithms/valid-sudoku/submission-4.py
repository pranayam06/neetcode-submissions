class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        rows = collections.defaultdict(set)  # 0: set of nums in row 0
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # x,y tuple [0,2] x [0,2]: set of nums in x,y

        for r in range(len(board)): 
            for c in range(len(board[0])): 
                tar = board[r][c]
                square = squares.get((r//3, c//3),{})
                if  tar == ".":
                    continue
                if tar in rows[r]:
                    return False  
                if tar in cols[c]:
                    return False 
                rows[r].add(tar)
                cols[c].add(tar)   

                if tar in square:
                    return False 
                
                squares[(r//3, c//3)].add(tar) 

        return True

                

                

        