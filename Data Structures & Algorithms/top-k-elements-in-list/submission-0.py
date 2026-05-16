class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        l = set(nums) 
        hm = {}
        for x in l:  
            count = nums.count(x)
            if nums.count(x) in hm:
                hm[count].append(x)
            else:
                hm[count] = [x]

            # if count in key, append to value list  
            # else, create list as value for key   
        
        output = [None]*k  
        print(hm)
        print(hm.keys())

        skeys = list(hm.keys())
        skeys.sort() 
        shm = {}
        for key in skeys:
            shm[key] = hm[key]

        for i in range(0, k):  
            tar = max(list(shm.keys()))
            output[i] = shm[tar][0]
            shm[tar].pop(0)
            if not shm[tar]:
                shm.pop(tar)

        return output



        

            
        


        

        
        

        