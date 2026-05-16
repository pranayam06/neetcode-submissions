# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        def samesub(x, y):
            if not y and not x: 
                return True 
            if not x or not y:
                return False 
            return (x.val == y.val) and samesub(x.left, y.left) and samesub(x.right, y.right)

        def same(x, y):  

            if samesub(x, y): 
                return True 
            if not x:
                return False
            return same(x.left, y) or same (x.right, y)  

        return same(root, subroot)