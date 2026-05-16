class Solution:

    def encode(self, strs: List[str]) -> str:  
        encd = ""
        for s in strs: 
            encd += s + "�"
        return encd

    def decode(self, s: str) -> List[str]: 
        decd = []
        j = 0
        for i in range(len(s)): 
            if s[i] == "�": 
                decd.append(s[j:i]) 
                j = i+1
        
        
        return decd