class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start times  
        # [[1,3],[1,5],[6,7]]
        # s = 6 >  - merge
        # e = 5  

        # merge on s < e 
        # return sorted list 

        intervals.sort()  

        s = intervals[0][0]
        e = intervals[0][1] 
        res = []

        for (t1, t2) in intervals[1::]: 
            if t1 > e:  
                res.append([s,e]) 
                s = t1
                e = t2
            else:
                e = max(e, t2) 
    
        res.append([s,e])  
        return res
