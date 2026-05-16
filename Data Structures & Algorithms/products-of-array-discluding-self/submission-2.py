class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1 
        for j in range(1, len(nums)):
            postfix *= nums[j]

        res = []
        res.append(prefix*postfix)


        for i in range(1, len(nums)):  
            if(i == len(nums)-1):
                postfix = 1
            elif (nums[i] == 0):
                postfix = 1
                for k in range(i+1, len(nums)):
                    postfix = postfix*nums[k] 
            else:
                postfix = postfix/nums[i]
            prefix = prefix*nums[i-1]
            res.append(int(prefix*postfix))

        return res
                

            


            