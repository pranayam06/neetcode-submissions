class Node: 
    def __init__(self, key=-1, value=-1):
        self.key = key 
        self.value = value 
        self.nxt = None
        self.prev = None

class LinkedList: 
    def __init__(self): 
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail 
        self.tail.prev = self.head
    
    def movetofront(self, node): 
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        self.addtofront(node)
    
    def addtofront(self, node): 
        first = self.head.nxt

        node.prev = self.head
        node.nxt = first

        self.head.nxt = node
        first.prev = node

        
    def removetail(self): 
        node = self.tail.prev
        old_prev, old_next = node.prev, node.nxt 
        old_prev.nxt = old_next 
        old_next.prev = old_prev
        return node
        # return node




class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.hmap = {}
        self.ll = LinkedList()
        self.size = 0
    

    def get(self, key: int) -> int:
        if key in self.hmap: 
            node=self.hmap[key]
            self.ll.movetofront(node)
            return node.value
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap: 
            node=self.hmap[key]
            self.ll.movetofront(node)
            node.value = value
        else:
            if self.size == self.cap: 
                removed = self.ll.removetail()
                del self.hmap[removed.key]
                self.size -=1 
            node = Node(key, value)
            self.hmap[key] = node
            self.ll.addtofront(node)
            self.size += 1
        
        
