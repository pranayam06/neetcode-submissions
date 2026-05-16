class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 # initialize the output 
        for i in range(32): # iterate through each bit in n
            bit = 1 & (n >> i) # extract bit i
            res += bit << (31-i) # assign that bit to its opposite side and add to output

        return res