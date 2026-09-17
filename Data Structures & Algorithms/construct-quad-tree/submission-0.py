"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        

        def dfs(u, d, l , r): 
            val = grid[u][l]

            for row in range(u, d):
                for col in range(l, r): 
                    if grid[row][col] != val: 
                        # break it up and return node  
                        tl = dfs(u, (d + u) // 2, l, (l + r) // 2)
                        bl = dfs((d + u) // 2, d, l, (l + r) // 2)
                        tr = dfs(u, (d + u) // 2,(l + r) // 2, r)
                        br = dfs((d + u) // 2, d, (l + r) // 2, r)
                        node = Node(False, False, tl, tr, bl, br)
                        return node 

            return Node(val, True, None, None, None, None)

        return dfs(0, len(grid), 0, len(grid[0]))


