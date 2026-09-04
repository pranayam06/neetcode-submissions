class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]: 

        adjlist = defaultdict(list) 
        for (a,b) in edges: 
            adjlist[a].append(b)
            adjlist[b].append(a)
        
        dp = {}
        seen = set()
        def dfs(node):
            cur = 0  
            seen.add(node)
            for nbor in adjlist[node]:
                if nbor not in seen: 
                    cur = max(cur, dfs(nbor))
            cur += 1 
            return cur 
        
        
        mht = float('inf')
        dp = defaultdict(list)
        for i in range(n): 
            seen = set()
            h = dfs(i)
            dp[h].append(i)
            mht = min(h, mht)
        print(mht)
            

        return list(dp[mht])
        

        

                    

        


        