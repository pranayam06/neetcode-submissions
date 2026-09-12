"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # assuming it is a connected graph, not a forest of connected components (obviously)
        # set a dummy node for the begining 
        # traverse each of the adjacent 
        # can use dfs or bfs bc we just need to create each possible node 
        # seen can be just ints of unique ids because less space 
        # for each neighbor create and traverse 

        seen = dict()
        # val to node 
        # set of integers 
        
        def dfs(root):
            if not root: 
                return None
            # create it 
            new_nbors = []
            seen[root.val]= Node(val=root.val, neighbors = new_nbors)

            # if seen already, we havent seen it in this path so we can just add to the list of its nbors 
            for nbor in root.neighbors:  
                # since its directed we need to make sure we grab node 
                if nbor.val not in seen: 
                    new_nbors.append(dfs(nbor))
                else: 
                    new_nbors.append(seen[nbor.val]) 
            
            return seen[root.val]
        
        return dfs(node)
            

                    


            















