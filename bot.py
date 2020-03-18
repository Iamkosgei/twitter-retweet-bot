import tweepy
import os


# auth
api_key = os.getenv("api_key")
api_secret_key = os.getenv("api_secret_key")
access_token = os.getenv("access_token")
token_secret = os.getenv("token_secret")

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, token_secret)
# auth

os.getenv("api_key")
os.getenv("api_secret_key")
os.getenv("access_token")
os.getenv("token_secret")


# init api
api = tweepy.API(auth)
# init api


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        if 'RT @' not in tweet.text:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            # print(tweet.text)
            # print(tweet)
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            if not tweet.retweeted:
                try:
                    print("retweeting " + str(tweet.id))
                    api.retweet(tweet.id)
                except Exception as e:
                    print("error " + str(e))

    def on_error(self, status_code):
        print(status_code)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=["flutter app", "flutterapp",
                       "flutterdev", "androiddev"])
