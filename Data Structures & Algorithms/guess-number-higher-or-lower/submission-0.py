# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0 
        r = n
        

        while (r>=l): 
            i = l + (r-l)//2
            ret = guess(i)
            if ret == 0:  
                return i
            if ret == 1:  
                l = i+1  
            if ret == -1:  
                r = i
        