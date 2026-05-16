class Solution:
    def jump(self, nums: List[int]) -> int:
        
        idx = 0
        ct = 0

        while(idx<len(nums)): 
            if idx == len(nums)-1:
                break
            if idx + nums[idx] >= len(nums) - 1:
                    ct += 1
                    break
            ct+=1

            num = nums[idx] 
            m = 0 
            temp = 0
            for j in range(idx+1, min(idx+num+1, len(nums))):
                if (nums[j] + j) > m:
                    temp = j
                    m = nums[j] + j
            idx = temp
            
        
        return ct