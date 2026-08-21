class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        reach = []
        for i in range(len(position)):
            reach.append((target- position[i]) / speed[i])
        ct = 0
        psr = zip(position, speed, reach)
        psr = sorted(psr, reverse=True)
        stack = []
        for p, s, r in psr:
            if stack and r > stack[0]:
                stack = []
                ct += 1
            stack.append(r)
        
        return ct+1
            

