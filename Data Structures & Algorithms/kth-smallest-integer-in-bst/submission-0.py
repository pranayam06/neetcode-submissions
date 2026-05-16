# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ct = 0
        self.res = 0
        
        def helper(node):
            if not node:
                return 
            helper(node.left)
            self.ct+=1    
            if self.ct == k:
                self.res= node.val 
            helper(node.right)
        
        helper(root)
        return self.res

            
            
