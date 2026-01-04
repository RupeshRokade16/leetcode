"""
Hashmap 1 = UserId mapped to set of followee ID 
Hashmap 2 = UserId mapped to list of (count, tweetID)

Follow, unfollow simply using hashmap 1
For getNewsFeed => Find the users followee's, get their list of (count, tweetID) and then solve mergeKSortedLists by keeping a ptr at the end of each list (since it is
being appended by timestamp, meaning the latest tweet by a followee will be at the
end of their respective list)

Put all these last index tweets in heap
pop from heap and decrement and push next item to index
the popped tweet id should be added to res


"""

class Twitter:
    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set) #userID -> followees set
        self.tweetMap = defaultdict(list) #userId -> tweets list

    def postTweet(self, userId: int, tweetId: int) -> None:
        #post the tweet to that particular followers list
        self.tweetMap[userId].append((self.count, tweetId)) #count acts as a timestamp
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #loop through all followers, get their tweets list from tweetMap
        #merge k sorted lists
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                #get last index of list
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                #append to minHeap
                minHeap.append((count, tweetId, followeeId, index - 1))
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, nextIndex = heapq.heappop(minHeap)
            res.append(tweetId)
            if nextIndex >= 0:
                count, nextTweetId = self.tweetMap[followeeId][nextIndex]
                heapq.heappush(minHeap, (count, nextTweetId, followeeId, nextIndex - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        #add to set
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #remove from set
        self.followMap[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
