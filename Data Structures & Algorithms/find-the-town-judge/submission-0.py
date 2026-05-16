class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # indegree people who trust you +1
        # outdegree people you trust -1

        net = [0] * (n+1) 

        for o, i in trust:
            net[o] -= 1
            net[i] += 1
        
        for i in range(1, n+1):
            if net[i] == n-1:
                return i
        return -1


