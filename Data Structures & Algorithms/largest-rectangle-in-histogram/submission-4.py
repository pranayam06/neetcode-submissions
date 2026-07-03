class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        s = deque()
        res = 0 

        for i, ht in enumerate(heights): 
            l = i
            while s and ht < s[-1][0]: 
                (val, _, l) = s.pop()
                res = max(res, val * (i-l)) 
            s.append( (ht, i, l))
        
        while s:
            h, _, idx = s.pop()
            res = max(res, h * (len(heights) - idx))
        
        return res