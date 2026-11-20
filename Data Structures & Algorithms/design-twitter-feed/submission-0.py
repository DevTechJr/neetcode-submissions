import heapq
from typing import Dict, List, Set


class Tweet:
    def __init__(self, tweet_id: int, time: int, author_id: int):
        self.tweet_id = tweet_id
        self.time = time
        self.author_id = author_id


class User:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.following: Set[int] = set()
        self.followers: Set[int] = set()
        # Stores tweets in chronological order (oldest -> newest)
        self.tweets: List[Tweet] = []

    def follow(self, target_id: int) -> None:
        if target_id != self.user_id:
            self.following.add(target_id)

    def unfollow(self, target_id: int) -> None:
        if target_id != self.user_id:
            self.following.discard(target_id)

    def post_tweet(self, tweet_id: int, time: int) -> None:
        self.tweets.append(Tweet(tweet_id, time, self.user_id))


class Twitter:
    def __init__(self, feed_limit: int = 10):
        self.users: Dict[int, User] = {}
        self.timer: int = 0
        self.feed_limit: int = feed_limit

    def _get_or_create_user(self, user_id: int) -> User:
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
        return self.users[user_id]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self._get_or_create_user(userId)
        self.timer += 1
        user.post_tweet(tweetId, self.timer)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []

        user = self.users[userId]
        # Users whose tweets can appear in the feed: followed users + self
        sources = set(user.following)
        sources.add(userId)

        # Python's heapq is a min-heap, so we push (-time, author_id, tweet_index, tweet_id)
        # to simulate a max-heap where the most recent tweet (largest time) is popped first.
        max_heap = []

        for author_id in sources:
            author = self.users.get(author_id)
            if author and author.tweets:
                last_idx = len(author.tweets) - 1
                latest_tweet = author.tweets[last_idx]
                heapq.heappush(
                    max_heap,
                    (-latest_tweet.time, author_id, last_idx, latest_tweet.tweet_id),
                )

        feed: List[int] = []
        while max_heap and len(feed) < self.feed_limit:
            neg_time, author_id, idx, tweet_id = heapq.heappop(max_heap)
            feed.append(tweet_id)

            # Push this author's next-older tweet if one exists
            next_idx = idx - 1
            if next_idx >= 0:
                older_tweet = self.users[author_id].tweets[next_idx]
                heapq.heappush(
                    max_heap,
                    (-older_tweet.time, author_id, next_idx, older_tweet.tweet_id),
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        follower = self._get_or_create_user(followerId)
        followee = self._get_or_create_user(followeeId)
        follower.follow(followeeId)
        followee.followers.add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.users and followeeId in self.users:
            self.users[followerId].unfollow(followeeId)
            self.users[followeeId].followers.discard(followerId)


# Example usage
# if __name__ == "__main__":
#     twitter = Twitter(feed_limit=10)
#     twitter.postTweet(1, 101)  # time 1: User 1 posts 101
#     twitter.postTweet(2, 201)  # time 2: User 2 posts 201
#     twitter.postTweet(2, 202)  # time 3: User 2 posts 202
#     twitter.follow(1, 2)       # User 1 follows User 2
#     print(twitter.getNewsFeed(1))  # [202, 201, 101]
#     twitter.unfollow(1, 2)     # User 1 unfollows User 2
#     print(twitter.getNewsFeed(1))  # [101]