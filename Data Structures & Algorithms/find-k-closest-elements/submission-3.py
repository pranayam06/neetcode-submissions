class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # bin search find l and r 
        s = 0
        l, r = 0, len(arr) - 1
        while (l < r):
            m = l + (r-l) // 2 
            if (arr[m] < x):
                l = m+1
            else:
                r = m 

        l = r-1

        res = []

        while len(res) < k:  
            if l < 0: 
                res.append(arr[r])
                r+=1
            elif r >= len(arr):
                res.append(arr[l])
                l-=1
            elif abs(arr[r] - x) >= abs(arr[l] - x):
                res.append(arr[l])
                l-= 1
            elif abs(arr[r] - x) < abs(arr[l] - x):
                res.append(arr[r])
                r+= 1
        return arr[l+1:r]



