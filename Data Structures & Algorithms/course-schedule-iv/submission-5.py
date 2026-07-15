class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjlist = defaultdict(list) 
        cache = dict()

        for (preq, crs) in prerequisites: 
            adjlist[crs].append(preq)
        

        def check(crs): 
            if not adjlist[crs]: 
                cache[crs] = set()
                return set()
            if crs in cache:
                return cache[crs]
            
            res = set()

            for preq in adjlist[crs]: 
                res = res | check(preq)
                res.add(preq)
            
            cache[crs] = res
            return res

        res_fin = []
        for u, v in queries: 
            if v in cache:             
                res_fin.append(u in cache[v])
            else:
                path = check(v)
                res_fin.append(u in path)

        return res_fin


             
