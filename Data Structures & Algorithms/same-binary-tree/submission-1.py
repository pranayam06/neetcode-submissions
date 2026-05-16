# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper (x,y): 

            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val == y.val and helper(x.left, y.left) and helper(x.right, y.right)


        return helper(p,q)