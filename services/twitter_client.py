import tweepy

class TwitterClient:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def post_tweet(self, text):
        try:
            tweet = self.api.update_status(text)
            return tweet.id
        except tweepy.TweepError as e:
            print(f"Error posting tweet: {e}")
            return None

    def reply_to_tweet(self, tweet_id, text):
        try:
            tweet = self.api.update_status(text, in_reply_to_status_id=tweet_id)
            return tweet.id
        except tweepy.TweepError as e:
            print(f"Error replying to tweet: {e}")
            return None

    def get_last_tweet(self, username):
        try:
            tweets = self.api.user_timeline(screen_name=username, count=1)
            return tweets[0] if tweets else None
        except tweepy.TweepError as e:
            print(f"Error retrieving tweet: {e}")
            return None
