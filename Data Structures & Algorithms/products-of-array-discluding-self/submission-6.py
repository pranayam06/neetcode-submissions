class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if you find more than one 0 itll all be 0 
        # if there is a 0, then everything except that will be 0 
        n = len(nums)
        pre = [1 for _ in range(n)]
        post = [1 for _ in range(n)]
        res = [1 for _ in range(n)]

        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]
            post[n-i-1] = post[n-i] * nums[n-i]
        
        for i in range(n):
            res[i] = pre[i] * post[i]
        return res


