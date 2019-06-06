#Sentimental Analysis
import tweepy

Consumer_key = "ZLKMoViTPxtuUqhtMa8urHmt3"
Consumer_secret = "nN9Rk1YPERYKdkcGzXcSEL04MUE3Qgv87RerTJZ7rVnYh1AGTx"
Token_key = "908703613345685509-Mecdzih111NKaNwbp6OPdPCgiu3p0Yo"
Token_secret = "cNHIId7zFQ8f20OokKu89EaTxlgr6WlOykS8fwU196Qht"
api = tweepy.OAuthHandler(consumer_key=Consumer_key, consumer_secret=Consumer_secret)
api.set_access_token(key=Token_key , secret=Token_secret)
tweets = tweepy.API(api)

def get_tweets():
    all_tweets = tweets.search('BTS')
    return all_tweets

for tweet in get_tweets():
    print(tweet.text)
