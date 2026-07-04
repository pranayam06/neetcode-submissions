import string

class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stk = []
        cur = ""

        for i, op in enumerate(s): 
            print(cur)
            print(stk)
            if op == "[": 
                continue
            elif ord('z') >= ord(op) >= ord('a'): 
                cur+=op
                if not stk:
                    res+=cur
                    cur = ""
            elif op == "]": 
                mult, idx = stk.pop()
                cur += (mult-1) * (cur[idx:])
                if not stk:
                    res+=cur
                    cur = ""
            else:
                if i and s[i-1].isnumeric():
                    mult, idx = stk.pop()
                    stk.append((mult * 10 + int(op), idx))
                else: 
                    stk.append((int(op), len(cur))) 
                continue 
        return res

            

