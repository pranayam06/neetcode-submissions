class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        # monotonically increasing

        s = deque()

        for i, ht in enumerate(heights): 
            idx = i
            while s and ht < s[-1][0]:
                h, _, idx = s.pop()
                res = max(res, h * (i-idx))

            s.append((ht, i, idx))
        while s:
            res = max(res, s[0][0] * (len(heights)-s[0][2]))
            s.popleft()
        

        return res
