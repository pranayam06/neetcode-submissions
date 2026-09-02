class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
         
        tot = sum(nums)
        if tot % k != 0:
            return False 
        sub_sum = tot // k
         # my initial thought is backtracking 
         # since we need to use k buckets, and we need to use each number exactly once, we can assign each number into a bucket based on the equal split reuqired
        
        dp = {}

        def dfs(i, arr):
            t = tuple(sorted(arr))
            if t in dp: 
                return dp[t]
            if i == len(nums): 
                return True 
            if nums[i] > sub_sum: 
                return False 
            num = nums[i]
            for j in range(len(arr)):
                if arr[j] + num <= sub_sum: 
                    arr[j] += num 
                    if dfs(i+1, arr):
                        dp[t] = True
                        return True
                    arr[j] -= num 
            dp[t] = False
            return False 
        
        return dfs(0, [0 for _ in range(k)])
            



