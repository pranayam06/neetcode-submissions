# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = int(-1001) 
        self.res = root.val

        def dfs(node):
            if not node: 
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            maxleft = max(l, 0)
            maxright = max(r, 0) 
            self.res = max(self.res, node.val + maxleft + maxright)
            return node.val + max(maxleft, maxright) 
        
        dfs(root)
        return self.res
