class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 0 is nothing 
        # negative is some number 
        # -100001 is some exist there but not a number
        nums = nums + [0]
        for i, num in enumerate(nums): 
            if num <0 or num > len(nums): 
                nums[i] = 0 

        for i, num in enumerate(nums): 
            if num != 0 and num != -100001:  
                if (abs(num) < len(nums)):  
                    if nums[abs(num)] == 0: 
                        nums[abs(num)] = -100001
                    else: 
                        nums[abs(num)] = -1* abs(nums[abs(num)]) 

        for i, num in enumerate(nums):
            if i == 0:
                continue 
            if num >= 0: 
                return i 


        return len(nums)
        
