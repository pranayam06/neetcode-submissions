class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # user id, personal tweets 
        self.following = defaultdict(set)
        self.ct = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.ct))
        #higher count is recenter
        self.ct += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = {}
        for user in list(self.following[userId]):
            users[user] = 0
        users[userId] = 0

        maxheap = []
        res = []
        for user, idx in users.items(): 
            n = len(self.tweets[user]) - 1
            if n-idx >= 0:
                tweet, ct = self.tweets[user][n - idx]
                heapq.heappush(maxheap,(-ct, tweet, user))
                users[user] += 1
        while maxheap and len(res) < 10: 
            print(maxheap)
            ct, tweet, user = heapq.heappop(maxheap)
            res.append(tweet)
            n = len(self.tweets[user]) - 1
            if n-users[user] >= 0:
                tweet, ct = self.tweets[user][n - users[user]]
                heapq.heappush(maxheap, (-ct, tweet, user))
            users[user] += 1 

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


        
