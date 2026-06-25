class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # find partition 
        l = 1
        r = n-1 
        while (l < r): 
            m = ((r - l) // 2) + l  

            left = mountainArr.get(m-1)
            mid = mountainArr.get(m)
            right = mountainArr.get(m+1)

            if left < mid < right: 
                l = m
            elif left > mid > right: 
                r = m 
            else: 
                break 
        
        # mid and l 

        center = m
        # search left
        l = 0
        r =  center + 1
        while (l < r): 
            m = (r - l) // 2 + l  
            print(m)

            val = mountainArr.get(m)

            if target > val: 
                l = m + 1
            elif target == val: 
                return m 
            else: 
                r = m 

        l = center
        r =  n
        while (l < r): 
            m = (r - l) // 2 + l  
            val = mountainArr.get(m)

            if target < val: 
                l = m + 1
            elif target == val: 
                return m 
            else: 
                r = m-1
        
        return -1
        

        

