class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # less than equal 
        # monotonically decreasing?
        res = [0 for _ in range(len(temperatures))]
        stack = [] # val, pos
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]: 
                stack.pop() 
            if stack: 
                res[i] = stack[-1][1] - i  
            stack.append((temperatures[i],i))
        return res
        

