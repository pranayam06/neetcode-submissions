class Solution:
    def trap(self, heights: List[int]) -> int:
        s = deque() #ht, i 
        res = 0
        for i, height in enumerate(heights):
            while s and s[-1][0] <= height: 
                valley = s.pop()
                if s: 
                    res += (min(s[-1][0], height) - valley[0]) * (i - s[-1][1] - 1)
            s.append((height,i)) 
        return res




            