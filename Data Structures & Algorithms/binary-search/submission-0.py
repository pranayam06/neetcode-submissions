class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) 
        

        while (r>l): 
            i = l + (r-l)//2
            if target == nums[i]:  
                return i
            if target > nums[i]:  
                l = i+1  
            if target < nums[i]:  
                r = i
        return -1  
            
            




