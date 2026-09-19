"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # its always going to be an immediate ancestor in one 
        def find(node, target):
            if not node: return False 
            if node == target: 
                return True
            return find(node.left, target) or find(node.right, target)
        
        # look up the tree first 
        par = p.parent
        child = p
        while par:  
            if par == q: 
                return par 
            if par.left == child:
                # traverse the right side  
                if find(par.right, q):
                    return par 
            if par.right == child:
                # traverse the right side  
                if find(par.left,q):
                    return par 
            child, par = par, par.parent
        
        # look down the tree 
        if find(p.right, q) or find(p.left, q): 
            return p 
        
        return None

            


        
