class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        l = 0  
        m = l
        r = len(nums) - 1
        while (l <= m and m <= r): 
            print(m) 
            print(l)
            print(r)
            if (nums[m] == 0): 
                tmp = nums[l] 
                nums[l] = nums[m]
                nums[m] = tmp
                if (l == m):
                    m = m+1
                l = l+1  
            elif (nums[m]==1): 
                m = m+1
            else:
                tmp = nums[r] 
                nums[r] = nums[m]
                nums[m] = tmp
                r = r-1  
            
        return nums
             




        