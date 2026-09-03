class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}

        def dfs(i, side): 
            if (i,side) in dp: 
                return dp[(i,side)]
            if i == len(stoneValue): 
                return 0 
            acc = 0 
            res_alice = -float('inf') 
            res_bob = float('inf')
            for j in range(0, 3): 
                if i + j >= len(stoneValue): 
                    break
                val = stoneValue[i+j]
                acc += val 
                if not side: 
                    res_alice = max(acc + dfs(i+j+1, (side+1) %2), res_alice) 
                else: 
                    res_bob = min(dfs(i+j+1, (side+1) %2) - acc, res_bob)

            if side: 
                dp[(i,side)] = res_bob
            else:
                dp[(i,side)] = res_alice
            return dp[(i,side)]

        end = dfs(0, 0)
        if end >0: 
            return 'Alice'
        elif not end: 
            return 'Tie'
        else:
            return 'Bob'
