class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0 
        r = len(people)-1
        people.sort()
        boats = 0
        
        while(l<=r):
            if people[r] + people[l] <= limit: 
                boats += 1 
                l += 1
                r -=1
            else: 
                boats+=1 
                r-=1
        
        return boats

            