class Solution:
    def reverse(self, x: int) -> int: 
        i = 0  
        maxbit = 0x7FFFFFFF
        output = 0  
        neg = x<0
        
        x = abs(x)
        while abs(x) > 0: 
            mod = x % 10 
            print(mod)
            x = int( x / 10 ) 
            output = 10 * output + mod  
            print(output)

            i+=1 
            if i == 9:  
                if (output > (maxbit / 10)) or (output == (maxbit / 10 ) & (x > (maxbit % 10))): 
                    return 0
        if neg: 
            print("here")
            return ~(output - 1)
        return output

            
        return output

        