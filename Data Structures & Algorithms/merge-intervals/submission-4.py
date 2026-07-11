class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        current_end = intervals[0][1] 
        current_start = intervals[0][0]
        res = []

        for (start, end) in intervals: 
            if start <= current_end: 
                current_end = max(end, current_end)
            else: 
                res.append((current_start, current_end))
                current_end = end
                current_start = start
        res.append((current_start, current_end))
        return res
            
