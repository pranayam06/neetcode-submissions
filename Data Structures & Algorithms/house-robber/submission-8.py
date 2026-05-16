class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums)+2)
        memo[0] = memo[1] = 0 

        def dfs(i):
            if memo[i+2] >= 0:
                return memo[i+2]
            else:
                memo[i+2] = max(dfs(i-1), nums[i] + dfs(i-2))
                return memo[i+2]
        
        return dfs(len(nums)-1)

        