class Solution:
    def rob(self, nums: List[int]) -> int:
        maxes = [-1] * (len(nums)+1) 
        maxes[0] = 0
        maxes[1] = nums[0] 
        

        for i in range(1, len(nums)):
            maxes[i+1] = max(nums[i] + maxes[i-1], maxes[i])
        print(maxes)
        return max(maxes[-1], maxes[-2])
        