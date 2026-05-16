class Solution:
    def climbStairs(self, n: int) -> int:


        def findsteps(n):

            if n == 1:
                return 1
            
            if n == 2: 
                return 2 
            
            return findsteps(n-1) + findsteps(n-2)
        
        return findsteps(n)



