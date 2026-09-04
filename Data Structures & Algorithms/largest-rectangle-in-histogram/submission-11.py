class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []  
        res = -1
        for i in range(len(heights)): 
            h = heights[i] 
            last = i
            
            while s and h < s[-1][0]: 
                (some, idx) = s.pop() 
                last = idx
                res = max(res, (i-idx) * some)
            s.append((h, last))
        
        n = len(heights)
        
        while s: 
            (h, i) = s.pop()
            res = max(res, (n-i)*h)
        
        return res


