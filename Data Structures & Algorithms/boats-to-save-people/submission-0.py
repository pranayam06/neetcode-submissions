class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int: 
        people.sort()
        count = 0  
        l, r = 0, len(people)-1

        while (r >= l):
            total = people[r] + people[l]
            if(r==l):
                r-=1
            elif(total > limit):
                r-=1
            elif (total <= limit):
                r-=1 
                l+=1
            count += 1
        
        return count
                


        

