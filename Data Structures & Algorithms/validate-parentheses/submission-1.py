class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        Map = {"}" : "{", "]" : "[", ")" : "("} 

        for c in s: 
            if c not in Map: 
                stack.append(c) 
                
            elif not stack or stack[-1] != Map[c]:
                return False
            else: stack.pop()

        return not stack
         




        i = 1
        k = []

        k.append(s[0]) 


        while (i < len(s)):   
            print(k)
            if s[i] == "[":  
                k.append("[") 
            if s[i] == "(":  
                k.append("(")
            if s[i] == "{":  
                k.append("{")
            
            if s[i] == "]": 
                if k[len(k) - 1] == "[":  
                    k.pop()  
                else: return False

            if s[i] == "}":
                if k[len(k) - 1] == "{": 
                    k.pop() 
                else: return False
            
            if s[i] == ")":
                if k[len(k) - 1] == "(": 
                    k.pop() 
                else: return False
                
            i+=1 

        print(k)
        return k == [] 
        
        


            


        