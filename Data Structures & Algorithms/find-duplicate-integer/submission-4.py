class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hash set would be O(n) time and O(n) space due to extra hash set 

        for i in range (len(nums)):
            if nums[abs(nums[i])-1] < 0: 
                
                return abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] *= -1
