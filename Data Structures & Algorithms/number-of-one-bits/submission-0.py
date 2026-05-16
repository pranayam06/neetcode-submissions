class Solution:
    def hammingWeight(self, n: int) -> int: 
        o = 0 
        for i in range (0,32):
             o += (1 & (n >> i))

        return o
            
        