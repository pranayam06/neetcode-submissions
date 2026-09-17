# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -1 * float('inf')
        # returns max height of the two subtrees
        def dfs(node): 
            nonlocal max_path
            if not node: 
                return 0 
            l = dfs(node.left) 
            r = dfs(node.right)
            max_path = max(node.val + l + r, max_path)

            return max(0, node.val + max(l, r))
        
        dfs(root)
        return max_path