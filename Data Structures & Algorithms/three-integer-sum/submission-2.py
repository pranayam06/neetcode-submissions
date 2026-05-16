class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        res = []

        nums.sort()
        for f in range(len(nums) - 2):
            if not f == 0 and nums[f] == nums[f-1]:
                continue
            l = f+1
            r = len(nums)-1            
            
            while (l < r):
                if not l == f+1 and nums[l] == nums[l-1]:
                    l+= 1 
                    continue
                if not r == len(nums)-1 and nums[r] == nums[r+1]:
                    r-=1
                    continue 
                 
                tot = nums[l] + nums[r]
                comp = 0-nums[f]

                if tot == comp:
                    res.append([nums[f], nums[l], nums[r]])
                    r-=1 
                    l+=1
                elif tot > comp:
                    r-=1
                elif tot < comp:
                    l+= 1
        return res
                
                
            



        