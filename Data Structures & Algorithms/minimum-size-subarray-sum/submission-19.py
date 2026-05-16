class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur = 0 
        l = 0
        res = 100001

        for r in range(len(nums)):
            cur += nums[r]
            print(cur)
            while cur >= target:
                res = min(res, r - l + 1)
                # move left pointer 
                cur -= nums[l]
                l+=1
        if res == 100001:
            return 0
        return res