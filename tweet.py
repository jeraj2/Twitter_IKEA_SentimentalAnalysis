import os
import tweepy
from dotenv import load_dotenv
import pandas as pd


load_dotenv()
print(os.getenv('API_KEY'))
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuth1UserHandler(
  consumer_key, 
  consumer_secret, 
  access_token, 
  access_token_secret
)

api = tweepy.API(auth)

tweets = api.search_tweets("Ikea", tweet_mode="extended")

for tweet in tweets:
    try:
        print(tweet.retweeted_status.full_text)
        print("=====")
    except AttributeError:
        print(tweet.full_text)
        print("=====")
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)
 
tweets_df = pd.DataFrame()    
for tweet in tweets_copy:
    hashtags = []
    try:
        for hashtag in tweet.entities["hashtags"]:
            hashtags.append(hashtag["text"])
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
    except:
        pass
    tweets_df = pd.concat([tweets_df,pd.DataFrame.from_records([{'user_name': tweet.user.name, 
                                               'user_location': tweet.user.location,\
                                               'user_description': tweet.user.description,
                                               'user_verified': tweet.user.verified,
                                               'date': tweet.created_at,
                                               'text': text, 
                                               'hashtags': [hashtags if hashtags else None],
                                               'source': tweet.source}])])
    tweets_df = tweets_df.reset_index(drop=True)
# show the dataframe

print(tweets_df.head())