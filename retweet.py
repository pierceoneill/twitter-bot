import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# tweet_list = api.favorites(screen_name='DavidDobrik', count=5)
# print(tweet_list)

# print the id for each of the tweets
#for tweet in tweet_list:
    #print(tweet.id)

# retweet a tweet.id
# tweet_id = 1231720300724793344
# api.retweet(tweet_id)

# retweet each teet
for tweet in api.favorites(screen_name='pierceoneill'):
    try:
        api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(e)