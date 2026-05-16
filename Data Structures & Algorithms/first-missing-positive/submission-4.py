class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range (len(nums)):
            if nums[i] <= 0 :
                nums[i] = len(nums) + 1
        
        for num in nums: 
            if(abs(num) > 0 and abs(num) <= len(nums)):
                nums[abs(num)-1] = abs(nums[abs(num)-1])*-1
        print(nums) 
        last = 1
        for k in range(len(nums)):
            if (nums[k] > 0):
                return k+1
        return len(nums) +1
            
