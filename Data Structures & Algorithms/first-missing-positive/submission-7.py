class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = [0 for _ in range(100001)]
        arr[0] = 1
        for num in nums: 
            if num >=0 and num <= 100001: 
                arr[num] =1 
        
        for i in range(len(nums)+1): 
            if arr[i] != 1: 
                return i  
        
        return len(nums)+1
        
