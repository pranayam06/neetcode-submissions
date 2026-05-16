class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        xorr = nums[0] 
        print (xorr)
        for i in range (1,len(nums)): 
            print (xorr)
            xorr ^= nums[i]
        
        return xorr

        