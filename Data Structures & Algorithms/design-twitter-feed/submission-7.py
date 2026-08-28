class Twitter:

    def __init__(self):
        self.followees = defaultdict(set)
        self.posts = defaultdict(list)
        self.ct = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.ct, tweetId))
        self.ct += 1 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followees[userId].add(userId)
        maxheap = []
        res = []
        for f in list(self.followees[userId]):
            post_ct = len(self.posts[f])
            if post_ct:
                #(-ct, f, post_ct, tweetId)
                (ct, tweet) = self.posts[f][post_ct -1]
                heapq.heappush(maxheap, (-ct, f, post_ct-1, tweet))
        while (len(res) < 10 and len(maxheap)):
            (_, f, idx, tweet) = heapq.heappop(maxheap)
            res.append(tweet)
            if idx: 
                (ct, tweet) = self.posts[f][idx -1]
                heapq.heappush(maxheap, (-ct, f, idx-1, tweet))
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None: 
        self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


        
