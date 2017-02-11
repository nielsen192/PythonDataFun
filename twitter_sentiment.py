import tweepy
from textblob import TextBlob

consumer_key = 'FW9Hb3avDPwVxtu12L2vrjvWb'
consumer_secret = 'sw16ehUJWrNu27t0nXHyVrXy7h6q2KgKVfS6KcjyqtK2W24Fgh'

access_token = '162134261-8nQbjlOWZ9V4ZzMIiqAUw36dkpac3ouBcFASaY9k'
access_token_secret = 'vkWRVTSzQ4swxCcTrs0z9646PxRmOvbUHDQeTrdbVuC6d'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
