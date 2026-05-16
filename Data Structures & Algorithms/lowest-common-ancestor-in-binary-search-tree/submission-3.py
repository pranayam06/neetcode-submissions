# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def helper(node, pval, qval):
            if not node: 
                return 
            if pval <= node.val <= qval:
                return node 
            elif qval <= node.val <= pval:
                return node  
            elif pval <= node.val:
                return helper(node.left, pval, qval)
            else:
                return helper(node.right, pval, qval)
        
        return helper(root, p.val, q.val)