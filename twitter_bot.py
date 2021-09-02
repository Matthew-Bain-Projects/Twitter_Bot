import requests
import tweepy

consumer_key = 0
consumer_secret = 0
access_token = 0
access_token_secret = 0

# Twitter requires oAuth2 to access its API:
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet_something(tweet):
    status = api.update_status(tweet)
    print(status.id)


