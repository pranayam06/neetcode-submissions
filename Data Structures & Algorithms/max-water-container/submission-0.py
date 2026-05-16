class Solution:
    def maxArea(self, heights: List[int]) -> int: 
        vol = 0

        for l in range(0, len(heights)): 
            for r in range(l+1, len(heights)):
                vol = max(vol, min(heights[l], heights[r]) * (r-l)) 

        return vol
        