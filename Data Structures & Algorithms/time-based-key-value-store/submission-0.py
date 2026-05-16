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
            while (l<r):
                m = l + ((r-l) // 2) 
                print("timestamp middle = " + str(arr[m][1]))
                if (arr[m][1] == timestamp):
                    return arr[m][0]
                elif (arr[m][1] > timestamp):
                    r = m-1
                else:
                    l = m+1 

            print(l)
            if arr[l][1] <= timestamp:
                return arr[l][0]
            elif arr[l][1] > timestamp and l != 0:
                return arr[l-1][0]
            elif l == 0:
                return ""
            else:
                return arr[l][0]

            

        
