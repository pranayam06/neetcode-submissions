"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = dict()
        
        cur = head
        new = dummy = Node(0, None, None)
        
        while (cur):
            # add cur to hmap 
            new.next = Node(cur.val, None, None)
            hmap[cur] = new.next 
            new = new.next 
            cur = cur.next 
        
        cur = head
        new = dummy.next

        while (cur):
            if not cur.random:
                new.random = None 
            else:
                new.random = hmap[cur.random]
            
            new = new.next 
            cur = cur.next 
        
        return dummy.next 


