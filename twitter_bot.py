import requests
import tweepy
import keys

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret
 

# Twitter requires oAuth2 to access its API:
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet_something(tweet):
    status = api.update_status(tweet)
    print(status.id)

tweet_something("Hello World! I'm testing out a little twitter bot. Come check out the project at: https://github.com/Matthew-Bain-Projects/Twitter_Bot")
