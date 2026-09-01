class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        glob_min = nums[0]
        glob_max = nums[0]

        cur_min = 0
        cur_max = 0
        tot = 0

        for num in nums: 

            cur_min = min(num, num + cur_min)
            cur_max = max(num, num+cur_max)

            tot += num 

            glob_min = min(glob_min, cur_min)
            glob_max = max(glob_max, cur_max)

        
        if glob_max <= 0: 
            return glob_max

        return max(tot - glob_min, glob_max)