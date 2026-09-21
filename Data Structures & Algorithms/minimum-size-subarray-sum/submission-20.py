class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0 
        cur_sum = 0 
        res = len(nums) + 1
        while (l <= r < len(nums)):
            cur_sum += nums[r] 
            while cur_sum >= target: 
                res = min(res, r-l+1)
                cur_sum -= nums[l]
                l+=1 
            r+= 1
        if res > len(nums): 
            return 0 
        return res


