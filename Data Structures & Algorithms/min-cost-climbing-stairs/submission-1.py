class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mincost = [-1] * n

        mincost[0] = cost[0]
        mincost[1] = cost[1]

        for i in range(2, n):
            one = mincost[i-2]
            two = mincost[i-1]
            mincost[i] = cost[i] + min(one, two)

        return min(mincost[n-1], mincost[n-2])