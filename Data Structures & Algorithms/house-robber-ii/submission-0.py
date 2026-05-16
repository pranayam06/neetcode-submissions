class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(arr):
            a, b = 0, arr[0]

            for i in range(1, len(arr)):
                a, b = b, max(arr[i] + a, b)  
        
            return b 
        
        return max(helper(nums[0: len(nums)-1]), helper(nums[1:len(nums)]))
        

        