# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.res = 0
        def dfs(node, ct): 
            if node: print(node.val)
            if not node: 
                return 0 
            l = dfs(node.left, ct) 
            if l == None: 
                return
            if l == ct-1: 
                self.res = node.val
                return 
            else: 
                r = dfs(node.right, ct-l-1) 
                if r==None: 
                    return 
            return l + r + 1

        dfs(root, k)
        return self.res



            
            










            
            