"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = dict() 

        if not node:
            return None
        
        #copy node 
        res = Node(1, None) 
        visited[1] = res

        def dfs(node, copy_node):
            for neighbor in node.neighbors:
                if neighbor.val in visited: 
                    copy_node.neighbors.append(visited[neighbor.val])
                else:
                    new = Node(neighbor.val, None)
                    copy_node.neighbors.append(new)
                    visited[neighbor.val] = new
                    dfs(neighbor, new) 

        dfs(node, res) 
        return res

            
