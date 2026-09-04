class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjlist = defaultdict(list) 
        indegree = defaultdict(int)
        isprereq = [set() for _ in range(numCourses)]

        for (preq, crs) in prerequisites: 
            adjlist[preq].append(crs) 
            indegree[crs] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0: 
                q.append(i)
        
        while q: 
            preq = q.popleft()
            for crs in adjlist[preq]: 
                isprereq[crs].add(preq)
                isprereq[crs].update(isprereq[preq])
                indegree[crs] -= 1
                if indegree[crs] == 0: 
                    q.append(crs)
                
            
        return [u in isprereq[v] for u,v in queries]
            

        




             
