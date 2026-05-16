class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adj list 
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        self.visited = set()
        def dfs(node):
            if node in self.visited: 
                return False
            self.visited.add(node)
            for nbor in preMap[node]:
                if dfs(nbor) == False:
                    return False
            self.visited = set() 
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True