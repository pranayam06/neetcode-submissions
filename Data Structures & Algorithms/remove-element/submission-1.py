class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        
        
        l = 0 
        r = len(nums)-1 

        while (l<=r):
            if nums[l] == val:
                nums[r], nums[l] = nums[l], nums[r]
                r = r-1
            else:
                l = l+1
        
        return l