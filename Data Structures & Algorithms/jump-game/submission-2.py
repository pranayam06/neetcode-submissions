class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = set()
        canReach.add(0)

        for i, num in enumerate(nums):
            if i in canReach: 
                for j in range(0, num+1):
                    canReach.add(i+j)
        return len(nums)-1 in canReach

