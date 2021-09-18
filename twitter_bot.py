import requests
import tweepy

consumer_key =
consumer_secret =
access_token = 
access_token_secret =
 

# Twitter requires oAuth2 to access its API:
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet_something(tweet):
    status = api.update_status(tweet)
    print(status.id)

tweet_something("Hello World!")
