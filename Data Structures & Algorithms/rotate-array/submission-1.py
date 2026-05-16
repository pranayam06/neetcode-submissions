class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        for i in range(len(nums)//2):
            nums[i], nums[-1*i-1] = nums[-1*i-1], nums[i]
            #reverse array 
        
        for j in range(k//2):
            nums[j], nums[k+ (-1*j-1)] = nums[k+ (-1*j-1)], nums[j]
            #reverse array 

        for l in range((len(nums)-k)//2):
            nums[k+l], nums[-1*l-1] = nums[-1*l-1], nums[k+l]
            #reverse array 