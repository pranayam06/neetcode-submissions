class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        res = []
        for (crs, preq) in prerequisites: 
            adjlist[crs].append(preq)
        path = set()
        done = set()
        
        def dfs(crs):  
            if crs in path: 
                return False 
            elif crs in done: 
                return True

            path.add(crs)
            
            for prereq in adjlist[crs]:
                if not dfs(prereq):
                    return False
            
            path.remove(crs)
            done.add(crs)
            res.append(crs)
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res



            
