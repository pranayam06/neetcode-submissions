class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * len(nums)

        for i, num in enumerate(nums):
            res[(i+k)%len(nums)] = num
        
        for j in range(len(nums)):
            nums[j] = res[j]