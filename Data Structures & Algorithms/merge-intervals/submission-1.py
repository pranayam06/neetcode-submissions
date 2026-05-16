class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])

        i = 0
        while i < len(intervals)-1:
            l = intervals[i]
            r = intervals[i+1]

            if l[1] >= r[0]:
                r[0], r[1] = min(l[0], r[0]), max(l[1],r[1])
                intervals.pop(i) 
            else:
                i+=1
        return intervals
                