class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        
        n = len(nums)
        xorr = n
        for i in range (0, n): 
            xorr ^= i ^ nums[i]
        
        return xorr


           



         


        