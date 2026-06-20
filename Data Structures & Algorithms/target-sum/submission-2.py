class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # need to keep track of the nums listed 
        # need to keep track of the index 

        memo = {}
        

        def dfs(i, tot):
            if (i, tot) in memo: 
                return memo[(i, tot)]
            if i == len(nums) and tot == target: 
                return 1 
            elif i >= len(nums):
                return 0
            else:
                memo[(i, tot)] = dfs(i+1, tot+nums[i]) + dfs(i+1, tot - nums[i]) 
                return memo[(i,tot)]
        return dfs(0, 0)

