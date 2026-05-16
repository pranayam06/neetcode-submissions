class Solution:
    def mySqrt(self, x: int) -> int: 

        l = 0 
        r = x
        

        while (r>=l): 
            i = l + (r-l)//2
            if x == i*i:  
                return i
            if x > i*i:  
                l = i+1  
            if x < i*i:  
                r = i-1
        return min(l,r) 
        