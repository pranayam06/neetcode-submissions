class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        de = set(deadends)
        seen = set()

        q = deque()
        q.append([0,0,0,0]) 
        turn = 0 

        while q: 
            turn += 1
            for _ in range(len(q)):
                arr = q.popleft()
                s = ''.join(map(str, arr))
                if s == target: 
                    return turn-1
                if (s in de) or (s in seen):
                    continue 
                seen.add(s)

                for i, num in enumerate(arr): 
                    q.append(arr[:i] + [(arr[i] + 1) % 10] + arr[i+1:]) 
                    q.append(arr[:i] + [(arr[i] - 1) % 10] + arr[i+1:]) 
        
        return -1 
        




            
                

