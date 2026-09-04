class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]: 
        if n ==1: 
            return [0]

        adjlist = defaultdict(list) 
        for (a,b) in edges: 
            adjlist[a].append(b)
            adjlist[b].append(a)

        q = deque()
        
        degrees = defaultdict(int)
        for i in range(n):
            degrees[i] = len(adjlist[i])
            if len(adjlist[i]) == 1: 
                q.append(i)
        
        while q:  
           
            if n <= 2: return list(q)
            for _ in range(len(q)):
                node = q.popleft() 
                n-=1

                for nbor in adjlist[node]: 
                    degrees[nbor] -= 1
                    if degrees[nbor] == 1: 
                        q.append(nbor)
        
        return list(q)
            

            

        

        

                    

        


        