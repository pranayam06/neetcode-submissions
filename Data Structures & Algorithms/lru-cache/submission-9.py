class Node: 
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # dummy nodes for safety
        self.left = Node(0,0) 
        self.right = Node(0,0) 
        self.left.next = self.right 
        self.right.prev = self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev
    
    def add(self, node):
        prev, nxt = self.right.prev, self.right 
        prev.next = node
        nxt.prev = node 
        node.next = nxt 
        node.prev = prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None: 
        #print(self.cache)
        if key not in self.cache.keys():
            if len(self.cache.keys()) == self.cap:
                lru = self.left.next
                del self.cache[lru.key] 
                print(self.left.next)
                self.remove(lru)  
                print(self.left.next)
            node = Node(key, value)
            self.add(node)
            self.cache[key] = node

        self.cache[key].val = value 
        self.remove(self.cache[key])
        self.add(self.cache[key])
        
            

