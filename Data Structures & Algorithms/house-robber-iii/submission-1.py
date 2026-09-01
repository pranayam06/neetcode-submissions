# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def is_leaf(node): 
            return not node.left and not node.right
        
        def helper(node):
            if is_leaf(node): 
                # take and don't take
                print((node.val, 0) )
                return (node.val, 0) 
            
            take_left = dont_left = 0
            take_right = dont_right = 0

            if node.left: 
                take_left, dont_left = helper(node.left) 
            if node.right: 
                take_right, dont_right = helper(node.right)

            take = node.val + dont_left + dont_right
            dont_take = max([take_left +take_right, take_left + dont_right, take_right + dont_left, dont_left + dont_right])

            return (take, dont_take)
        
        return max(helper(root))
             

