from textblob import TextBlob
my_demo_text = TextBlob("Bad Boy.")
my_demo_text2 = TextBlob("Very Good Boy.")
my_demo_text3 = TextBlob("The sun rises in the East.")
print(my_demo_text.sentiment)   #Sentiment(polarity=-0.6999999999999998, subjectivity=0.6666666666666666)
print(my_demo_text2.sentiment)  #Sentiment(polarity=0.9099999999999999, subjectivity=0.7800000000000001)
print(my_demo_text3.sentiment)  #Sentiment(polarity=0.0, subjectivity=0.0)

#polarity lies between [-1,1]
#negative polarity -> negative opinion
#positive polarity -> positive opinion
#subjectivity [0,1] -> 0 = Objective, 1 = Subjective