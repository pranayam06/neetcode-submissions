class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        

        dp = defaultdict(int)
        dp[0] = 1
        for i in range(1, target + 1): 
            for num in nums: 
                dp[i] += dp[i-num] 
        
        return dp[target]
            

