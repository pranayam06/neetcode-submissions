class Solution:
    def multiply(self, num1: str, num2: str) -> str: 
        res = 0 

        for i in range(len(num1)-1, -1, -1): 
            for j in range(len(num2)-1, -1, -1):
                zeroes = len(num1) - 1 - i + len(num2) - 1 - j  
                res += int(num1[i]) * int(num2[j]) * 10**zeroes
        
        return str(res)

        