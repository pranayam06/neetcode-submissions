class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [-1] * len(cost)
        n = len(cost)

        mincost[0] = cost[0]
        mincost[1] = cost[1]

        for i in range(2, len(cost)):
            one = mincost[i-2]
            two = mincost[i-1]
            mincost[i] = cost[i] + min(one, two)
        
        print(mincost)
        return min(mincost[n-1], mincost[n-2])