# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str: 
        q = deque()
        if not root: 
            return ""
        arr = []
        q.append((0,root))
        lvl = 1
        while q: 
            
            l = len(q)
            for i in range(l): 
                
                val = q.popleft()  
                if not val: 
                    arr.append(" ")
                    continue
                else:
                    prev, cur = val
                arr.append(str(cur.val))
                if cur.left:
                    q.append((2*prev, cur.left))
                else: 
                    q.append(None)
                if cur.right:
                    q.append((2*prev+1, cur.right)) 
                else: 
                    q.append(None)
            
            
            lvl += 1
        print(arr)
        return "#".join(arr)



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: 
            return None
        arr = data.split("#")
        dq = deque()
        dq.append(TreeNode(arr[0]))
        res = dq[0]
        i = 1

        while(dq):
            cur = dq.popleft()
            if i < len(arr): 
                left_val = arr[i]
                if left_val != " ": 
                    cur.left = TreeNode(int(left_val))
                    dq.append(cur.left)
            i += 1
            if i < len(arr): 
                right_val = arr[i]
                if right_val != " ": 
                    cur.right = TreeNode(int(right_val))
                    dq.append(cur.right)
            i+= 1
        return res
                    

