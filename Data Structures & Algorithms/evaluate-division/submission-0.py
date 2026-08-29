class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjlist = defaultdict(list)
        for i, [a,b] in enumerate(equations):
            adjlist[a].append((b, values[i]))
            adjlist[b].append((a, 1.0/values[i]))
        
        
        def dfs(a,b): 
            if (a not in adjlist) or (b not in adjlist):
                return -1.0 
            if a == b: 
                return 1.00 
            if a in seen: 
                return -1.0
            seen.add(a)
            for var, quotient in adjlist[a]: 
                rest = (dfs(var, b))
                if (rest >= 0.0):
                    return quotient * rest 
            
            return -1.00

        res = []

        for a, b in queries: 
            seen = set()
            res.append(dfs(a, b))

        return res
            
