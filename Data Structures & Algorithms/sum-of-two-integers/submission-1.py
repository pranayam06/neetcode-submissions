class Solution:
    def getSum(self, a: int, b: int) -> int: 
        output = 0 
        carry = 0
        for i in range (0, 32):  
            abit = 1 & (a >> i)
            bbit = 1 & (b >> i)
            output += (abit ^ bbit ^ carry) << i  
            carry = (abit + bbit + carry) >> 1 

       
        if output > 0x7FFFFFFF:
            return ~(output ^ 0xFFFFFFFF)
        else: return output


            
        