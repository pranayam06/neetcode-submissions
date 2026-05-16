class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = deque()

        res = []
        for i in range(0, len(nums)):
            while s and s[0][1] <= i-k: 
                s.popleft()
            while s and s[-1][0] <= nums[i]: 
                s.pop()
            s.append((nums[i], i))   
            if i >= k-1:
                res.append(s[0][0])
        
        return res

