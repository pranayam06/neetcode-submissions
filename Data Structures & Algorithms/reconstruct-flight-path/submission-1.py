class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjlist = defaultdict(list)

        for start, end in tickets:
            adjlist[start].append([end,0])
        for key, val in adjlist.items():
            val.sort()

        out = []
        
        def dfs(tickets_left, airport, res):
            if tickets_left == 0:
                return res.copy()
                res.append(ap)
            for i, (ap, used) in enumerate(adjlist[airport]):
                if not used:
                    adjlist[airport][i][1] = 1
                    res.append(ap)
                    val = dfs(tickets_left-1, ap, res)
                    res.pop()
                    adjlist[airport][i][1] = 0
                    if val:
                        return val
            return None
        
        return dfs(len(tickets), 'JFK', ['JFK'])
        
