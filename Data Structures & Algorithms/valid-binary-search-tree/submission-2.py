# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(lower, upper, node):
            if not node:
                return True  
            if lower and lower.val >= node.val:
                return False 
            if upper and upper.val <= node.val:
                return False
            else:
                return dfs(lower , node, node.left) and dfs(node, upper, node.right)
        
        return dfs(None, None, root)