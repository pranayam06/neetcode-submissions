class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[i]:
                x = s.pop()
                res[x] = i-x
            s.append(i) 
        
        return res

