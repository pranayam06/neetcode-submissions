class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        squares = collections.defaultdict(list)

        for r in range(9):
            for c in range(9):   
                #print(board[r][c])
                if (board[r][c] == "."):
                    continue
                else:
                    sidx = int((r//3)*3 + (c//3) )
                    print(sidx)
                    if board[r][c] in rows[r]: 
                        return False 
                    elif board[r][c] in cols[c]: 
                        return False 
                    elif board[r][c] in squares[sidx]:
                        return False
                    else:
                        rows[r].append(board[r][c])
                        cols[c].append(board[r][c])
                        squares[sidx].append(board[r][c]) 

        
        return True





                

                

        