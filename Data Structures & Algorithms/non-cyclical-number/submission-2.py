class Solution:
    def isHappy(self, n: int) -> bool: 
        slow = n   
        fast = self.sumOfSquares(n) 
        print (slow)
        print (fast) 
        if fast == 1:
                return True

        while slow != fast: 
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(fast) 
            fast = self.sumOfSquares(fast)  

            if fast == 1:
                return True
            
        return False





    def sumOfSquares(self, n: int):
        sum = 0
        while n > 0:
            sum += pow((n % 10),2)
            n = n // 10
        
        return sum


              

        