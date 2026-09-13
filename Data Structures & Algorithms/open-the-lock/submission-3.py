class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        # use bfs because we want minimum 
        # prune at deadends 
        # do mod 

        de = set(deadends)
        seen = set()

        q = deque()
        q.append("0000")
        if "0000" in de: 
            return -1
        turns = 0 
        while q: 
            print(q)
            for _ in range(len(q)): 
                str_comb = q.popleft()
                if str_comb == target: 
                    return turns
                

                comb = list(map(int, list(str_comb)))
                for i in range(4): 
                    plus = ''.join(map(str, comb[:i] + [(comb[i] + 1) % 10] + comb[i+1:]))
                    if plus not in de and plus not in seen: 
                        seen.add(plus)
                        q.append(plus)
                    minus = ''.join(map(str,comb[:i] + [((comb[i] - 1) % 10)] + comb[i+1:]))
                    if minus not in de and minus not in seen: 
                        seen.add(minus)
                        q.append(minus)
            turns += 1
    
        return -1



