class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        class UnionFind():
            def __init__(self, n):
                self.arr = [i for i in range(n+1)]
                self.rank = [1] * (n+1)

            def find(self, x):
                if self.arr[x] != x:
                    self.arr[x] = self.find(self.arr[x])
                return self.arr[x]

            
            def union(self, a, b):
                findA = self.find(a)
                findB = self.find(b)

                if findA == findB:
                    return False 
                
                else:
                    if self.rank[findA] < self.rank[findB]:
                        self.arr[findA] = findB
                        self.rank[findB] += self.rank[findA]
                    else:
                        self.arr[findB] = findA
                        self.rank[findA] += self.rank[findB]
                
                return True 
        uf = UnionFind(len(edges))
        for a,b in edges:
            if not uf.union(a,b):
                return [a,b]




                


