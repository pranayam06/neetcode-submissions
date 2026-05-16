class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prereq adj list 
        adjlist = defaultdict(list)
        for crs, pre in prerequisites: 
            adjlist[crs].append(pre)
        
        res = []
        visited = set() # used to track output
        path = set() # used to determine cycles 

        def dfs (crs):
            if crs in path: 
                return False 
            if crs in visited: 
                return True
            path.add(crs)
            for pre in adjlist[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True 

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
