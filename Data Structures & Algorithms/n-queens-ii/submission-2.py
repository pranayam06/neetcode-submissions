class Solution:
    def totalNQueens(self, n: int) -> int:
        # n horizontals n verticals 
        # 4n-2 horizontals 
        res = 0
        taken_col = set() # enumerate which column is taken 
        taken_neg = set()
        taken_pos = set()

        def backtrack(row):
            nonlocal res 
            if row == n:
                res+= 1
                return

                
            for col in range(n):
                pos = row - col 
                neg = n - col - row 
                # pick the column 

                if col not in taken_col and pos not in taken_pos and neg not in taken_neg:
                    taken_col.add(col)
                    taken_pos.add(pos)
                    taken_neg.add(neg)
                    backtrack(row+1)
                    taken_col.remove(col)
                    taken_pos.remove(pos)
                    taken_neg.remove(neg)
    
        backtrack(0)
        return res



        
