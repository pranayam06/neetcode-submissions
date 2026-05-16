class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1 
         
        while (l < r):
            m = l + (r-l)//2 
            if (nums[m] < nums[r]):
                r = m
            else:
                l = m+1

        pt = l

        l, r = 0, len(nums) - 1

        while(l <= r):
            m = l + (r-l) // 2 
            idx = (pt + m) % len(nums)
            cur = nums[idx]
            if cur == target: 
                return idx
            elif cur < target:
                l = m + 1 
            else:
                r = m - 1
        return -1





        