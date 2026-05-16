class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max elem of window at each step 
        dq = deque()  # val, idx 
        res = [] 
        # fixed subarray 
        for r in range(len(nums)):
            print(dq)
            print(res)
            while dq and dq[-1][0] < nums[r]:
                dq.pop()
            dq.append((nums[r], r))

            while dq and dq[0][1] <= r-k: 
                dq.popleft()
            if r >= k-1: 
                res.append(dq[0][0])
        
        return res