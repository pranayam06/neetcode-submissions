"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0 
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        print(start)
        print(end)

        s = 0
        e = 0
        ct = 0
        while (s < len(intervals) and e < len(intervals)):

            if start[s] < end[e]:
                ct += 1 
                s += 1
            elif start[s] >= end[e]:  
                res = max(res, ct)
                e+=1 
                ct -= 1 
        res = max(res, ct)
        return res
