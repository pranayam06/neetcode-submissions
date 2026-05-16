class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(n, stack, cur): 
            if not stack and n == 0: 
                # stack empty and n = 0 
                print(cur)
                res.append(cur[::])
            else:
                if stack:
                    stack.pop()
                    dfs(n, stack, cur + ")")
                    stack.append(")")
                if n > 0: 
                    stack.append("(")
                    dfs(n-1, stack, cur + "(")
                    stack.pop() 
        
        dfs(n, [], "")
        return res

                

            