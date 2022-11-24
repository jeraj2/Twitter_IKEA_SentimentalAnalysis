import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')
class MyStreamer(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.id)
        print(tweet.text)
        print("======")

streamer = MyStreamer(bearer_token)
streamer.add_rules(tweepy.StreamRule("#Ikea lang:en"))

streamer.filter()