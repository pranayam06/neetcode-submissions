# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ct = 0 
        # track max value along each path 
        def dfs(node, val): 
            if not node: 
                return 
            if val <= node.val:
                self.ct+=1
            dfs(node.left, max(node.val, val))
            dfs(node.right, max(node.val, val)) 

        dfs(root, -101)
        return self.ct

