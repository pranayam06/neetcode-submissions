"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        last = 0

        for interval in intervals: 
            s = interval.start
            e = interval.end
            if s < last: 
                return False 
            else: 
                last = e 
        
        return True

        
