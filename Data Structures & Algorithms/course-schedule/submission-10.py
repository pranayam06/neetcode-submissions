class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 

        # simple cycle detection 
        adjlist = defaultdict(list)
        for preq in prerequisites: 
            adjlist[preq[0]].append(preq[1])

        print(adjlist)
        
        # key = course, value = prereqs 
        def dfs(course, path):
            for preq in adjlist[course]:
                if preq in path: 
                    return False 
                else: 
                    path.add(preq)
                    if not dfs(preq, path): 
                        return False 
                    path.remove(preq)
            return True
            



        for i in range(numCourses):
            visited = set([i])
            if not dfs(i, visited):
                return False 
            else: 
                continue 
        return True

        