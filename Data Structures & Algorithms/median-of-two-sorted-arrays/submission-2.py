class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        half = (m + n) // 2  
        if n > m: 
            nums1, nums2 = nums2, nums1 
            n, m = m, n
        # nums2, n is smaller 

        l2, r2 = 0, n

        while (l2<=r2): 
            j = l2 + (r2-l2) // 2 
            i = half - j

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                if (m+n) % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left2 > right1:  
                r2 = j - 1
            elif left1 > right2:
                l2 = j + 1
             




            