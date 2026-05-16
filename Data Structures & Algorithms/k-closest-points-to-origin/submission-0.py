class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            x = point[0]
            y = point[1]
            h.append([x**2 + y**2, [x,y]])
        
        heapq.heapify(h)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        return res