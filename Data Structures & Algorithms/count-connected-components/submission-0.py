class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0 
        visited = set() 

        adjlist = defaultdict(list)
        for a, b in edges:
            adjlist[a].append(b)            
            adjlist[b].append(a) 
        
        def dfs(node): 
            if node not in visited:
                visited.add(node)
                for neighbor in adjlist[node]:
                    dfs(neighbor)

        while len(visited) < n: 
            for i in range(n):
                if i not in visited:
                    dfs(i)  
                    print(visited)
                    break 
            res+= 1
        
        return res

