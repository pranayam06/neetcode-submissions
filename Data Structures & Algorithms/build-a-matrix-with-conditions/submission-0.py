class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        
        def get_order(rowConditions): 
            opensUp = defaultdict(set)
            requires = defaultdict(set)
            indegree = defaultdict(int)

            # build adjacency list and indegrees 
            for above, below in rowConditions: 
                requires[above].add(below)
                opensUp[below].add(above)
            
            q = deque()
            rowOrder = []

            for key in range(1,k+1):
                l = requires[key] 
                indegree[key] = len(l)
                if len(l) == 0: 
                    q.append(key)
                    rowOrder.append(key)
            n= k

            # row stuff 
            while q:  
                val = q.popleft() 
                if n == 0: 
                    return None
                n-=1

               
                for num in list(opensUp[val]): 
                    indegree[num] -= 1  

                    if indegree[num] == 0: 
                        rowOrder.append(num)
                        q.append(num)

            if n != 0: 
                return None
            return rowOrder

        rowOrder = get_order(rowConditions)
        print(rowOrder)
        if not rowOrder: 
            return []
        colOrder = get_order(colConditions)
        print(colOrder) 

        if not colOrder: 
            return []
       

        rows = [0 for _ in range(k+1)]
        for i in range(len(rowOrder)): 
            val = rowOrder[i]
            rows[val] = k-i-1
        
        cols = [0 for _ in range(k+1)]

        for i in range(len(colOrder)): 
            val = colOrder[i]
            cols[val] = k-i-1
        
        res = [[0 for _ in range(k)] for _ in range(k)]

        for val in range(1, k+1):
            r = rows[val]
            c = cols[val]
            res[r][c] = val

        return res




        
        
        


        # capture a list of lists that has the order for row and column 
        # if their indegree becomes 0 in the same loop (2 values become available at the same time )