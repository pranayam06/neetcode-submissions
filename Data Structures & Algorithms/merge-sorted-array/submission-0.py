class Solution: 
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        r1 = m-1 
        r2 = n-1
        target = n+m-1 

        while (r1>=0 and r2 >=0): 
            print(nums1)
            if (nums1[r1] >= nums2[r2]): 
                tmp = nums1[r1]
                nums1[target]= tmp
                target -= 1
                r1 -= 1
            else:
                tmp = nums2[r2]
                nums1[target]= tmp
                target -= 1
                r2 -= 1 

        while r2 >= 0:
            nums1[target] = nums2[r2]
            r2-=1
            target -=1



        


        