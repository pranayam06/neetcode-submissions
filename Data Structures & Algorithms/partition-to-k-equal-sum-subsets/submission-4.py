class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        dp = {}
        tot = sum(nums)
        if tot % k != 0:
            return False 
        sub_sum = tot // k
         # my initial thought is backtracking 
         # since we need to use k buckets, and we need to use each number exactly once, we can assign each number into a bucket based on the equal split reuqired
        
        used = [False for _ in range(len(nums))]



        def dfs(i, k, subset):
            u_bits = tuple(used)
            key = (u_bits, subset, k)
            if key in dp: 
                return dp[key] 
            if k == 0: 
                dp[key] = True
                return True 
            if subset == sub_sum: 
                dp[key] = dfs(0, k-1, 0)
                return dp[key] 
            elif i == len(nums):
                dp[key] = False
                return False
            
            if used[i]: 
                dp[key]= dfs(i+1, k, subset)
                return dp[key]
            else:
                used[i] = True 
                if dfs(i+1, k, subset + nums[i]):
                    dp[key] = True 
                    return dp[key] 
                used[i] = False
                if dfs(i+1, k, subset):
                    dp[key] = True
                    return True 
            dp[key] = False
            return False
        
        return dfs(0,k, 0)
        
            



