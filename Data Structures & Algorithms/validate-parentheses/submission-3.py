class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        hmap = {"(": ")", "[": "]", "{": "}",}


        for char in s:
            if char in hmap:
                stack.append(char)
            else:
                if not stack:
                    return False  
                elif not hmap[stack.pop()] == char:
                    return False 
        
        return not stack
                