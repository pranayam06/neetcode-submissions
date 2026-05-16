class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        # prereq adj list 
        adjlist = defaultdict(list)
        for crs, pre in prerequisites: 
            adjlist[crs].append(pre)
        
        res = []
        visited = set() # used to track output
        path = set() # used to determine cycles 

        def dfs (crs): 
           if crs in path: 
            return None
           else: 
            path.add(crs)

            visited.add(crs)
            for preq in adjlist[crs]: 
                if preq in path: 
                    return None
                if preq not in visited: 
                    if not dfs(preq):
                        return None
            if crs not in res: res.append(crs)
            path.remove(crs)
            return res
        
        for i in range(n):
            if not dfs(i): 
                return []
        
        return res



                
