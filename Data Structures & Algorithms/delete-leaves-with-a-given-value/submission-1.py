# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        # traverse down, 
        # when you recurse back upwards, you can check the leaf node state of each node 

        def fun(node): 
            if not node: 
                return False
            
                
            del_left = fun(node.left)
            del_right = fun(node.right) 

            if del_left: 
                node.left = None 
            if del_right: 
                node.right = None 
            
            return not node.left and not node.right and node.val == target

            # check left and right 
            # and delete 
        

        fun(root)
        if not root.left and not root.right and root.val == target:
            return None

        return root

            
