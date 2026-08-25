class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # shortest interval that query[j] sits in 
        intervals.sort()
        queries_sorted = list(enumerate(queries)) 
        queries_sorted.sort(key = lambda x: (x[1], x[0]))
        intervals_heap = []
        res = [0 for _ in range(len(queries))]

        i = 0



        for idx, val in queries_sorted: 
            while i < len(intervals):
                (s, e) = intervals[i]
                if s <= val and e >= val:
                    heapq.heappush(intervals_heap,(e-s+1, s, e))
                if s > val:
                    break
                i+=1

            if not len(intervals_heap): 
                res[idx] = -1
                continue
            while (intervals_heap and intervals_heap[0][2] < val):
                (length, s, e) = heapq.heappop(intervals_heap)
            if not len(intervals_heap): 
                res[idx] = -1
                continue
            (length, s, e) = intervals_heap[0]
            res[idx] = length 
        return res
        

            

                
            

        return []