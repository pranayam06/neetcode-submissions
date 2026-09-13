class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False

        adjlist = defaultdict(list)
        for a, b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a) 
        
        self.visited = set()

        def dfs(node, par):
            self.visited.add(node)

            for nbor in adjlist[node]: 

                if nbor == par: 
                    continue 
                if nbor in self.visited: 
                    return False 
                
                if not dfs(nbor, node):
                    return False
            return True

            
        
        res = dfs(0,-1)
        if not (len(self.visited) == n): 
            return False
        else:
            return res
