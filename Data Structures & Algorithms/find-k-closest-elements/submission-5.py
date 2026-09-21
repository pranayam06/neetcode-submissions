import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find using binary search 
        idx = bisect.bisect_left(arr, x)

        l = idx-1 
        r = l+1
        

        while (True): 
            
            # compare l and r 
            left = float('inf')
            if l >= 0: 
                left = x-arr[l]
            right = float('inf')
            if r < len(arr): 
                right = arr[r] - x
            if left <= right: 
                if r-l == k: 
                    return arr[l:r]
                l -= 1 
            else: 
                if r-l == k:
                    return arr[l+1: r+1]
                r+= 1
        return arr 



                


            
            