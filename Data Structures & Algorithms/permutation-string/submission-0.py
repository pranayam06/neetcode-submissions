class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)  
        r = 0 
        l=0
        hmap = defaultdict(int)
        for char in s1:
            hmap[char] += 1

        while (l <= len(s2) - length):  
            print(l)
            print(r)
            print (hmap)
            if l + length == r: 
                return True 
            if hmap[s2[r]] > 0: 
                hmap[s2[r]] -= 1
            else: 
                if(s2[l] in s1):
                    hmap[s2[l]] += 1 
                    r-=1   
                l+= 1   
            r+=1 
             

        return False


            
            



            
            
            
