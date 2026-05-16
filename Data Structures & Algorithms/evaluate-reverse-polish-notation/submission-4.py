class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        stack = []

        for c in tokens: 
            print(stack)
            if c== "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop()) 
            elif c == "-":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1-op2)
            elif c == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(math.trunc(op1/op2)) 
            else: 
                stack.append(int(c))
        
        return stack.pop()

        