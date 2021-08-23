import tweepy

API_KEY='W40tnQaZV8qiTomanopbHfByA'
API_SECRET='7Lo257Q0DiT18iwgsfrJuxBeXhyZkpW9MYod4g0skzS51Lz67u'
ACCESS_TOKEN='1429054152827674625-Vtf4NR1nvwWAzzWZnGvWo7k0WkEpEO'
ACCESS_SECRET='syejZ9vSzoZyzzPMWpfabphC5QeptIAqPLMolypbnzJYp'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# tweepy retweet likes function
def lambda_handler(event, context):
    for tweet in api.user_timeline('Intel_Sky', count=10):
        try:
            api.retweet(tweet.id)
        except tweepy.TweepError as e:
            print(e)
    return print("done.")