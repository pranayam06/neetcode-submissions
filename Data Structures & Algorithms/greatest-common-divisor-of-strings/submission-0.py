class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1 
        # str1 has the shorter length 

        len1 = len(str1)
        len2 = len(str2)

        def check(i):
            if len1%i or len2%i:
                return False 
            f1, f2 = len1 // i, len2 //i 
            return str1[:i] * f1 == str1 and str1[:i] * f2 == str2


        for i in range(len(str1), 0, -1):
            if check(i):
                return str1[:i] 
        return ""
            