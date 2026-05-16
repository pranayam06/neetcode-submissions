class Solution:
    def rob(self, nums: List[int]) -> int:
        maxes = [-1] * (len(nums)+1) 
        maxes[0] = 0
        maxes[1] = nums[0] 
        
        for i in range(1, len(nums)):
            maxes[i+1] = max(nums[i] + maxes[i-1], maxes[i])
        return maxes[-1] 

        a, b = 0, nums[0]

        for i in range(1, len(nums)):
            a, b = b, max(nums[i] + a, b),  
        
        return b

        