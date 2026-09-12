class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2 
        small = 0
        # find max value less than or equal target 
        memo = {}
        def dfs(i, cur): 
            nonlocal small
            if i == len(stones) or cur == target: 
                return abs((total - cur) - cur)
            if (i,cur) in memo:
                return memo[(i,cur)]
            
            memo[(i, cur)] = min(dfs(i+1, cur), dfs(i+1, cur + stones[i]))
            return memo[(i, cur)]

        return dfs(0, 0)
        
    

            

