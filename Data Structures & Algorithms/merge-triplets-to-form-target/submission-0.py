class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # find a match for each where the other two are <= 
        # 3n search 
        found = [False] * 3
        x = target[0]
        y = target[1]
        z = target[2]

        for a,b,c in triplets: 
            if a == x and b <= y and c<= z:
                found[0] = True
            if b == y and a <= x and c<= z:
                found[1] = True
            if c == z and a <= x and b<= y:
                found[2] = True
        
        return found == [True, True, True]
