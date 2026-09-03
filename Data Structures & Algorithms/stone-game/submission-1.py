class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(l, r, side): 
            if (l,r) in dp: 
                return dp[(l,r)]
            if r < l: 
                return 0 
            
            take_l = dfs(l+1, r, (side+1)%2) 
            take_r = dfs(l, r-1, (side+1)%2)
            if not side: 
                # alice 
                dp[(l,r)] = max(piles[l] +take_l, piles[r] + take_r)
                return dp[(l,r)]
            else: 
                dp[(l,r)] = min(take_l- piles[l], take_r- piles[r])
                return dp[(l,r)]

        
        return dfs(0, len(piles)-1, 0) > 0
            # return difference in score 
            # > 0 is alice's win



    

                 