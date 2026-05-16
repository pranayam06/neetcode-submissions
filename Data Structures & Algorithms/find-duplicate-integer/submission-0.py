class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hash set would be O(n) time and O(n) space due to extra hash set 

        nums.sort()
        for i in range (len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
