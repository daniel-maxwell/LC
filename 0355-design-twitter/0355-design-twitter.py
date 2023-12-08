class Twitter:

    def __init__(self):
        self.users = {} # user : (following<set>, feed<heap>)
        self.tweets = {} # user : queue
        self.time = 3 * (10**4)
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId in self.tweets:
            self.tweets[userId].appendleft((self.time, tweetId))
        else: 
            self.tweets[userId] = deque([(self.time, tweetId)])

        # push tweet to feed for all followers
        for user, info in self.users.items():
            
            if userId in info[0]:
                heapq.heappush(self.users[user][1], (self.time, tweetId))

        # push tweet to users feed
        if userId in self.users:
            heapq.heappush(self.users[userId][1], (self.time, tweetId))
        else:
            self.users[userId] = [set(), [(self.time, tweetId)]]

        self.time -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.users:
            if not self.users[userId][1]: return []
            else:
                return [tweet[1] for tweet in heapq.nsmallest(10, self.users[userId][1])]
        else:
            self.users[userId] = [set(), []]
            return []
        

    def follow(self, followerId: int, followeeId: int) -> None:

        # If we have registered this user....
        if followerId in self.users: 
            if followeeId not in self.users[followerId][0]:
                # add the followee to the set of followers for this user
                self.users[followerId][0].add(followeeId)
                
                # if the followee has any tweets
                if followeeId in self.tweets:
                    # push those tweets to the followers feed
                    for tweet in self.tweets[followeeId]:
                        heapq.heappush(self.users[followerId][1], tweet)

        # Otherwise, if this user isn't registered yet...
        else:
            # Create the user
            self.users[followerId] = [set([followeeId]), []]

            # if the followee has any tweets
            if followeeId in self.tweets:

                # push those tweets to the newly created users' feed
                self.users[followerId][1] = list(self.tweets[followeeId])


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId][0]:
            self.users[followerId][0].remove(followeeId) # remove the account from the users following set

            if followeeId in self.tweets: # if person beign unfollowed has tweets...
                newFeed = []
                deleteIds = set([tweet[1] for tweet in self.tweets[followeeId]])
                
                for tweet in self.users[followerId][1]:
                    if tweet[1] not in deleteIds:
                        newFeed.append(tweet)
                
                heapq.heapify(newFeed)
                self.users[followerId][1] = newFeed

        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)