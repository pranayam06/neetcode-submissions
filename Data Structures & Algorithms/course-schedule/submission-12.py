class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjlist = defaultdict(list)
        for crs, pre in prerequisites: 
            adjlist[crs].append(pre)
        seen = set()
        memo = dict()
        def dfs(crs): 
            if crs in memo: 
                return memo[crs]
            for preq in adjlist[crs]: 
                if preq in seen: 
                    memo[crs] = False
                    return False 
                seen.add(preq)
                if not dfs(preq):
                    memo[crs] = False

                    return False
                seen.remove(preq)
            memo[crs] = True

            return True 
        
        for i in range(numCourses): 
            seen = set([i])
            if not dfs(i): 
                return False 
        return True

