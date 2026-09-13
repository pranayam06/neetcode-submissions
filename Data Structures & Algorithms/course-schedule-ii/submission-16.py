class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adjlist = defaultdict(list)
        preq2crs = defaultdict(list)

        for crs, preq in prerequisites: 
            adjlist[crs].append(preq)
            preq2crs[preq].append(crs)
        
        indegrees = defaultdict(int)
        q = deque()
        for i in range(numCourses): 
            indegrees[i] = len(adjlist[i])
            if len(adjlist[i]) == 0: 
                q.append(i)
        n = numCourses
        while q:
            done = q.popleft()
            if n == 0: 
                return []
            n-= 1
            res.append(done)
            for crs in preq2crs[done]: 
                indegrees[crs]-= 1 
                if indegrees[crs] == 0:
                    q.append(crs) 
        if n == 0: 
            return res 
        else: 
            return []

            



