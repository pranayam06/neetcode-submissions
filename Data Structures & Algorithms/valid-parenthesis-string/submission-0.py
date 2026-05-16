class Solution:
    def checkValidString(self, s: str) -> bool: 
        left = []
        ast = []

        for i in range(len(s)): 
            if s[i] == "(":
                left.append(i)
            elif s[i] == "*":
                ast.append(i)
            else:
                if left:
                    left.pop()
                elif ast:
                    ast.pop()
                else:
                    return False
        while left:
            if not ast:
                return False
            if left[-1] < ast[-1]:
                left.pop()
                ast.pop()
            else:
                return False 
        return True
                



        