class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        for p in path.split("/"):
            val = p.strip("/")
            if len(val): 
                dirs.append(val)

        
        s = []

        for dir in dirs: 
            print(s)
            if dir == "..": 
                if s: s.pop()
                continue
            elif dir == ".":
                continue 
            else: 
                s.append(dir)
        
        return ("/" + "/".join(s))