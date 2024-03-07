#Sentimental Analysis
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
Consumer_key =" "
Consumer_secret = " "
Token_key = " "
Token_secret = " "
#Twitter authentication
api = tweepy.OAuthHandler(consumer_key=Consumer_key, consumer_secret=Consumer_secret)
api.set_access_token(key=Token_key , secret=Token_secret)
tweets = tweepy.API(api)
print("Hello World")


#function to extract tweets from the given keyword
def get_tweets():
    all_tweets = tweets.search('')
    return all_tweets

count = 0
positivity = 0
negativity = 0
neutral_tweets = 0
for tweet in get_tweets():
    my_SA = TextBlob(tweet.text)
    count += 1
    if my_SA.sentiment[0] > 0.0:
        positivity += 1
    elif my_SA.sentiment[0] < 0.0:
        negativity += 1
    elif my_SA.sentiment[0] == 0:
        neutral_tweets += 1

perc_neutral = neutral_tweets/count
perc_positive = positivity/count
perc_negative = negativity/count

print(perc_neutral)
print(perc_positive)
print(perc_negative)
#graph for positive and negative tweets 
labels = 'Positive', 'Neutral', 'Negative'
sizes = (perc_positive,perc_neutral,perc_negative)
plt.show(plt.pie(sizes,explode=(0.1,0,0),labels=labels)) #builds a graph on the basis of the data we obtained from tweets 
