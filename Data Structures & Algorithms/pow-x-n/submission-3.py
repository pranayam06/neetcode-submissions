class Solution:
    def myPow(self, x: float, n: int) -> float: 

        def helper(x, n): 
            print(x,n)
            
            if x == 0:
                return 0
            if n == 1: 
                return x  
            if n == 0: 
                return 1 
            
            if (n % 2 == 0):
                return helper(x*x, n/2)
            else:
                return helper(x*x, n//2) * x
        
        if n < 0: return 1/helper(x, abs(n))
        else: return helper(x, abs(n))

        
        
        
        