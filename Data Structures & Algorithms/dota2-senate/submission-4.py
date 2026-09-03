class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # two queues one for R one for D 
        Rq = deque()
        Dq = deque()
        for i, side in enumerate(senate): 
            if side == 'R':
                Rq.append(i)
            else:
                Dq.append(i)
        ct= 0 

        while(Rq or Dq): 
            if not Rq: 
                return 'Dire'
            if not Dq:
                return 'Radiant' 
            if Rq[0] == ct:
                Rq.append(Rq.popleft())
                Dq.popleft()
            elif Dq[0] == ct:
                Dq.append(Dq.popleft())
                Rq.popleft() 
            ct = (ct+1) % len(senate)
        
        
