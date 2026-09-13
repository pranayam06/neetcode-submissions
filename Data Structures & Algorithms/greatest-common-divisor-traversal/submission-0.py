class DSU: 
    def __init__(self, n): 
        self.arr = [i for i in range(n)]
        
    def union(self, a, b): 
        para = self.find(a)
        parb = self.find(b)
        self.arr[parb] = para


    def find(self,a): 
        par = self.arr[a]
        if par == a: 
            return a 
        else: 
            return self.find(par)
    
    def check(self): 
        par = self.find(0)
        for i in range(len(self.arr)): 
            if self.find(i) != par: 
                return False 
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        dsu = DSU(n)
        # index each num by their index in nums arr 

        for i in range(n): 
            for j in range(i+1, n):
                a = nums[i]
                b = nums[j]
                if math.gcd(a,b) > 1: 
                    dsu.union(i, j)
        
        return dsu.check()




