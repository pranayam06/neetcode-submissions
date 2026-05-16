class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0,0,0] # 5, 10, 20 

        for b in bills: 
            print(change) 
            print(b)
            if(b == 5):
                change[0] += 1 
            elif b == 10: 
                change[1] += 1
                if change[0] == 0: 
                    return False 
                else: 
                    change[0] -= 1
            else: 
                # assert b == 20
                change[2] += 1 
                if change[1] > 0 and change[0] > 0: 
                    change[1]-= 1
                    change[0] -= 1
                elif change[0] >= 3:
                    change[0] -= 3
                else:
                    return False 

        return True
 
            