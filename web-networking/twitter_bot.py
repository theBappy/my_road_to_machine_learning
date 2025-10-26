import tweepy
import time

print("Testing The Bot")

api_key = "API key"
api_secret = "API key secret"
access_token = "access token"
access_token_secret = "access token secret"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if not status.retweeted and status.in_reply_to_status_id is None:
            print(status.text)
        try:
            api.retweet(status.id)
            print("Retweeted")
        except tweepy.TweepyError as e:
            print(e.reason)

    def on_error(self, status_code):
        if status_code == 420:
            print("Error 420: Enhance your calm - Rate Limited")
            return False
        
my_stream_listener = MyStreamListener()
my_stream = tweepy.Stream(auth=api.auth, listener=my_stream_listener)

keywords = ["#Python", "#python", "#programming", "#coding"]
my_stream.filter(track=keywords, languages=["en"])



