class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        self.followers[userId].add(userId)
        for followeeId in self.followers[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                time, currId = self.tweets[followeeId][index]
                heap.append((time, currId, followeeId, index - 1))

        heapq.heapify(heap)
        count = 0
        
        while heap:
            time, currId, followeeId, index = heapq.heappop(heap)
            res.append(currId)
            count += 1

            if count == 10:
                break

            if index >= 0:
                time, currId = self.tweets[followeeId][index]
                heapq.heappush(heap, (time, currId, followeeId, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
