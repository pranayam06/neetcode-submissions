class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        res = []
        for i, c in enumerate(s):
            lastIndex[c] = i
        start = 0
        end = 0 
        print(lastIndex)

        for j in range(len(s)): 
            if lastIndex[s[j]] > end: 
                end = lastIndex[s[j]] 
            if j == end: 
                res.append(end-start+1)
                start = j+1
                end = j+1
        
        return res
            
            
