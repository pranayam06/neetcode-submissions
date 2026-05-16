class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int: 
        nums.sort()
        lowest = 0

        for num in nums: 
            if num <= 0:
                continue
            elif num==lowest+1 or num == lowest:
                lowest = num
            else: 
                return lowest+1
        return lowest+1








