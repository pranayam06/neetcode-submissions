class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        hm = dict()
        for i, num in enumerate(numbers):
            hm[num] = i
        
        for i in range(len(numbers)): 
            comp = target - numbers[i]
            if comp in hm and hm[comp] != i:
                return [min(i+1, hm[comp]+1),max(i+1, hm[comp]+1) ]



            

        