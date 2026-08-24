class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [-1] 
        res = -1
        stack = [] # (height, pos)
        for i in range(len(heights)): 
            while (stack and heights[i] <= stack[-1][0]): 
                (height, idx) = stack.pop()
                last_idx = -1 
                if stack: 
                    last_idx = stack[-1][1]
                res = max(res, height*(i-last_idx-1))
            stack.append((heights[i], i))
        
        return res



    