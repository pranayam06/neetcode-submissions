class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            ctmax = 0
            for j in range(0, i):
                if (nums[i] > nums[j] and count[j] > ctmax):
                    ctmax = count[j]
            count[i] = ctmax + 1
        print(count)
        return max(count)


