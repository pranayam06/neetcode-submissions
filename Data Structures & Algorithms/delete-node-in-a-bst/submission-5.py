# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        

        def reroot(node, rep): 
            if rep: 
                if not node: 
                    return rep 
                else: 
                    node.right= reroot(node.right, rep)
                    return node

            if not node: 
                return node
            if node.left and node.right: 
                node.left.right = reroot(node.left.right, node.right)
                return node.left

            if node.left: 
                return node.left
            return node.right


        def dfs(par, node, left):
            # found parent , side
            # find target 
            # if xor left xor right then just replace 
            # if both then replace with left and move right subtree to 
            if not node: 
                return 
            if node.val == key: 
                if left: 
                    par.left = reroot(node, None)
                    return 
                par.right = reroot(node, None)

                return
            dfs(node, node.left, True )
            dfs(node, node.right, False ) 
            return 

        dummy = TreeNode(0, None, root)
        dfs(dummy, root, False)
        return dummy.right
                
            