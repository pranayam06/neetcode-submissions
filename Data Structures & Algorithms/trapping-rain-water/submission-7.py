class Solution:
    def trap(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1 
        left_max = heights[l]
        res = 0
        right_max = heights[r]

        while (l < r): 
            if left_max < right_max: 
                res += max(0, left_max - heights[l])
                l += 1 
                left_max = max(left_max, heights[l])
            else: 
                res += max(0,right_max - heights[r])
                r -= 1 
                right_max = max(right_max, heights[r])
            
        return res


                

