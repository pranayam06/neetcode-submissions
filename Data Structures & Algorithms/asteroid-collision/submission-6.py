class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for ast in asteroids:
            if ast < 0 and not s: 
                s.append(ast)
            elif ast < 0 and s[-1] > 0:
                while(s and s[-1] > 0): 
                    if abs(ast) > s[-1]:
                        s.pop()
                    elif abs(ast) == s[-1]:
                        s.pop()
                        break
                    else: break 
                else: s.append(ast)
            elif ast < 0 and s[-1] < 0:
                s.append(ast)
            elif ast > 0:
                s.append(ast)
        
        return s



