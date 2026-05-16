class TimeMap:

    def __init__(self):
        self.hmap = dict() # key = key, value = [value][timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append([value, timestamp])
        else:
            self.hmap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str: 
        print(self.hmap)
        if not key in self.hmap:
            return ""
        else: 
            # bin search
            arr = self.hmap[key]
            l, r = 0, len(arr) - 1
            res = ""
            while (l<=r):
                m = l + ((r-l) // 2) 
                if (arr[m][1] <= timestamp):
                    res = arr[m][0]
                    l = m+1
                else:
                    r = m-1
            return res
