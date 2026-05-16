class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            print('analyzing ' + str(i))
            while s and temperatures[s[-1]] < temperatures[i]:
                count = 0
                idx = s.pop() 
                print('popped ' + str(temperatures[idx]))
                count += i-idx
                res[idx] = count
            
            s.append(i)
        
        return res