class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = [defaultdict(int) for _ in range(len(nums) + 1)]
        memo[0][0] = 1

        for i in range(1, len(nums) + 1): 
            for tot, ct in memo[i-1].items():
                memo[i][tot+nums[i-1]] += ct 
                memo[i][tot-nums[i-1]] += ct 
        return memo[len(nums)][target]


