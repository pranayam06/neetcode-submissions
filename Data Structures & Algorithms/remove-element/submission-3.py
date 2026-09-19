class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # swap each element with a num at the end of the list 
        l = 0 # num we look at 
        r = len(nums)- 1 # next num we want to swap with 

        while (l <= r): 
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1  
            else:
                l += 1 
            
        
        return l 
