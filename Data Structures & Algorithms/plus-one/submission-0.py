class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        last = len(digits)-1 
        if digits[last] < 9:
            digits[last] += 1
            return digits  
        
        i = last 
        
        digits[i] +=1  
        print(digits[i])
        while digits[i] == 10:  
            print("here")
            digits[i] = 0 
            if i == 0:
                digits.insert(0, 1) 
                return digits
            i -= 1   
            print(i)
            digits[i] +=1   
        
        return digits


        