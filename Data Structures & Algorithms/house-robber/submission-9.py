class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, nums[0] # guaranteed 

        for num in nums[1:]: 
            a, b = b, max(b, num + a)
        
        return max(a, b)