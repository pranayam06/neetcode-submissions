class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort()
        print(nums)
        res = []
        for f in range(len(nums)-2):  
            if (f > 0 and nums[f] == nums[f-1]):
                continue
            l = f+1 
            r = len(nums)-1 
            while (l<r):
                print(nums[f])
                print(nums[l])
                print(nums[r])
                comp = -1 * nums[f]
                total = nums[l] + nums[r]
                if (total < comp): 
                        l+=1
                elif (total > comp):
                    r-=1
                else: 
                    res.append(list((nums[f], nums[r], nums[l])))
                    l+=1
                    while (nums[l] == nums[l-1] and l<r):
                        l+=1
        
        return res

        