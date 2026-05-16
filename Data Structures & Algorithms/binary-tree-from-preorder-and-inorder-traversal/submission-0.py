# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inordermap = {val: idx for idx, val in enumerate(inorder)}  
        self.pre_idx = 0

        def helper(l, r):
            if l > r:
                return 
            else:  
                node = TreeNode(preorder[self.pre_idx], None, None)
                root_idx = inordermap[preorder[self.pre_idx]]
                self.pre_idx+=1
                node.left = helper(l, root_idx-1)
                node.right = helper(root_idx+1, r)
                return node
        
        return helper(0, len(inorder)-1)






