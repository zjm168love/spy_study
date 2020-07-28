import tweepy
auth = tweepy.OAuthHandler("your_consumer_key", "your_consumer_key_secret")
auth.set_access_token("your_access_token", "your_access_token_secret")
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)