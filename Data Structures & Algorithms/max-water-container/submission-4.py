class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        res = 0

        while (l < r): 
            left_height = heights[l]
            right_height = heights[r]
            res = max(res, min(left_height, right_height) * (r-l))
            if left_height <= right_height: 
                l+=1 
            else:
                r-=1

        return res

