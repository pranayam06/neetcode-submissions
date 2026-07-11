class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        # val, idx
        res = []

        for i, num in enumerate(nums):
            while q and q[0][1] <= i - k: 
                q.popleft()
            while q and q[-1][0] < num: 
                q.pop()
            q.append((num, i))
            if i >= k-1: 
                res.append(q[0][0])
        return res
