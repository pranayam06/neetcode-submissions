class Solution:
    def maxArea(self, heights: List[int]) -> int: 
        l, r = 0, len(heights)-1
        area = 0
        while (l < r and r <len(heights)): 
            barR = heights[r]
            barL = heights[l]
            area = max(area, (r - l) * min(barR, barL))

            if barR == barL:
                l+=1
            elif barR > barL:
                l+=1
            else:
                r-=1
        
        return area