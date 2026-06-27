class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjlist = defaultdict(list)
        for from_i, to_i, price_i in flights: 
            adjlist[from_i].append((to_i, price_i)) 
        
        self.res = 100000000

        def dfs(node, cur_cost, stops): 
            if node == dst: 
                self.res = min(self.res, cur_cost)
                return 
            if stops == k+1: 
                return
            if cur_cost > self.res: 
                return 
            for (to, price) in adjlist[node]: 
                dfs(to, cur_cost + price, stops+1)
        
        dfs(src, 0, 0)
        if self.res == 100000000:
            return -1 
        else: return self.res
            


