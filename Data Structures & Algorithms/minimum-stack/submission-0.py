class MinStack:

    def __init__(self):
        self.stack = [] 
        self.pstack = []

    def push(self, val: int) -> None:
        self.stack.append(val) 
        if (len(self.pstack)==0 or val < self.pstack[-1]):
            self.pstack.append(val)
        else:
            self.pstack.append(self.pstack[-1])

    def pop(self) -> None:
        tmp = self.stack.pop()
        self.pstack.pop()
        

    def top(self) -> int: 
        return self.stack[-1]

        

    def getMin(self) -> int: 
        return self.pstack[-1]
        
