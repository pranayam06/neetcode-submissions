class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        anaS = Counter(s) 
        anaT = Counter(t)
        return anaS==anaT
        