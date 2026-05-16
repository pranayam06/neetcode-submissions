class Solution:
    def tribonacci(self, n: int) -> int:
        one, two, three = 0, 1, 1

        for i in range(n): 
            # 0 , 1 , 2
            tmp = one + two + three 
            one, two, three = two, three, tmp 
        
        return one