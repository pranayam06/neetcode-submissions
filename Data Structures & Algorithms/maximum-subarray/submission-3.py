class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ct = -1001 
        res = -1001
        for i in range(len(nums)):
            ct = max(nums[i] + ct, nums[i]) 
            res = max(res, ct)
        return res
