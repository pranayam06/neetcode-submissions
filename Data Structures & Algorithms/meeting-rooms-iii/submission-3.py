class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # some heap to find unused room 
        # count how many times a number got popped off 
        # some heap to handle the room with the earliest start time

        # sort the meetinsg 
        # all of them start unused 
        # keep a heap of the earliest end time so when you delay a meeting then put the end times in a heap 
        used = defaultdict(int) 
        unavailable = []
        available = [(i, 0) for i in range(n)]
        # maintain available ones 
        # maintain the end times 

        meetings.sort()
        for (s, e) in meetings:
            
            while unavailable and unavailable[0][0] <= s: 
                time, room = heapq.heappop(unavailable)
                heapq.heappush(available, (room, time)) 
            if available: 
                # just take the first room 
                room, time = heapq.heappop(available)
                used[room] += 1
                heapq.heappush(unavailable, (e, room))
            else: 
                if unavailable: 
                    # clear up unavailable 
                    time, room = heapq.heappop(unavailable)
                    used[room] += 1
                    # take the first one 
                    heapq.heappush(unavailable, (max(time,e) + e - s, room))

        
        
        s = list(used.items())
        s.sort(key = lambda x: (-x[1], x[0]))
        return s[0][0]



             

