class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int: 
        edges = []
        for i, [x,y] in enumerate(points): 
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                edges.append((abs(x2-x) +abs(y2-y), i, j))
        
        edges.sort()
        dsu = DSU(len(points))
        res = 0 
        ct_edges = 0
        for dist, i, j in edges: 
            x, y = points[i], points[j]
            if (not dsu.union(i, j)): 
                continue
            ct_edges += 1
            res += dist 
            if ct_edges == len(points)-1: 
                return res
            
        
        return res
        
























        