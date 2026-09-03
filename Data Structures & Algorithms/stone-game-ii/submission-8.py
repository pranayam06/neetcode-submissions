class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # max you can take doubles each time 
        dp = {}
        def dfs(M, i, side): 
            if (M,i,side) in dp: 
                return dp[(M,i, side)]
            if i == len(piles): 
                return [0,0]
            acc = 0
            res = [0,0]
    
            for j in range(0, 2*M):
                if (i + j) >= len(piles): 
                    break
                acc += piles[i+j] 
                new_M = max(j+1,M)
                [A, B] = dfs(new_M, i+j+1, (side+1)%2)
                if not side:
                    if A + acc > res[0]:
                        res = [A + acc,B]
                else:
                    if B + acc > res[1]:
                        res = [A,B+acc]
            dp[(M,i,side)] = res
            return res
        
        res = dfs(1, 0, 0)
        return res[0]



                