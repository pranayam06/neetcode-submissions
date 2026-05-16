# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def helper(node, p, q):
            #node will always exist atp
            if node.val == p or node.val == q:
                return node
            if node.val >= p and node.val >= q: 
                return helper(node.left, p, q)
            if node.val > min(p,q) and node.val < max(p,q): 
                return node
            if node.val <= p and node.val <= q: 
                return helper(node.right, p, q)

        return helper(root, p.val, q.val)