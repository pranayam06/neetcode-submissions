class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjlist = defaultdict(list)

        for src, dest in sorted(tickets)[::-1]:
            adjlist[src].append(dest)
        
        res = []
        
        def dfs(src):
            while adjlist[src]:
                dest = adjlist[src].pop()
                dfs(dest)
            res.append(src)

        dfs('JFK')
        return res[::-1]
                

