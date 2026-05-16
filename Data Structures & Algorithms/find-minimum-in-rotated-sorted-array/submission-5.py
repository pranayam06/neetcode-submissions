class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0 
        r = len(nums) - 1
        def check(idx):
            if nums[idx] >= nums[(idx+1) % len(nums)]:
                return 0 
            elif nums[idx] >= nums[0]:
                return 1
            elif nums[idx] < nums[0]:
                return -1

        while ( l <= r):
            m = l + ((r - l) // 2) 
            print(m)
            cur = check(m) 
            print(cur)
            if cur == 0:
                return (nums[(m+1) % len(nums)])
            elif cur == 1:
                l = m+1
            else:
                r = m-1
        
            