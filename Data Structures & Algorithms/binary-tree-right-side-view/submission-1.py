# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
        que = deque([]) 
        if root: que.append(root) 
        res = []


        while (que):
            length = len(que) 
            res.append(que[-1].val)
            for i in range(length):
                cur = que.popleft()
                if cur.left: 
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        
        return res 

        