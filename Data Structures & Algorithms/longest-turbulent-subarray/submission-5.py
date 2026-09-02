class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cmp = -1
        cur_max = 1
        res = 0 
        for i, num in enumerate(arr): 
            if i == 0: 
                continue
            if cmp<0: 
                cmp = arr[i] > arr[i-1]
                cur_max += 1
            if num == arr[i-1]: 
                cur_max = 1 
                cmp = -1
            elif cmp<0: 
                cmp = arr[i] > arr[i-1]
                cur_max += 1
            elif cmp:
                if num < arr[i-1]: 
                    cmp = 0
                    cur_max += 1
                else: 
                    cur_max = 2
            else: 
                if num > arr[i-1]: 
                    cmp = 1
                    cur_max += 1
                else: 
                    cur_max = 2
            res = max(cur_max, res)
        res = max(cur_max, res)

        return res
            

