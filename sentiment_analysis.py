
import tweepy
import re
import pandas as pd
import itertools
import collections
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from textblob import TextBlob

# This file assumes you have created a list of tweets as detailed in the collect_tweets.py file within this repository

## Sentiment Analysis

# There are numerous forms of sentiment analysis, each with its own strengths and drawbacks
# Sentiment analysis refers to the use of natural language processing in order to ascertain the attitude of speech toward a specific topic. 

# Simple Polarity Sentiment Analysis
# This form of SA assigns a score of positive, neutral or negative to a text extract based on its word content. Each non-stop word is
# tallied and the text is assigned a score between -1 and 1. Scores above 0 are deemed positive and vice versa. 

# Using the same structure as in collect_tweets.py, we collect tweets based on a chosen hashtag
tweets = tweepy.Cursor(api.search,
              q="#dominiccummings -filter:retweets",
              lang="en",
              since="2020-05-20").items(100)
              
# Iterate through the text section of each tweet in order to evaluate its sentiment
for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

    if analysis.sentiment[0] > 0:
        print('Positive')
    elif analysis.sentiment[0] < 0:
        print('Negative')
    else:
        print('Neutral')
        
# In order to effectively visualise this, we will need to once again create a pandas dataframe but with our new sentiment columns
user_data = [[tweet.user.created_at, remove_characters(tweet.user.name), tweet.user.location,
              remove_characters(tweet.text), TextBlob(tweet.text).sentiment[0],
              'Positive' if TextBlob(tweet.text).sentiment[0] > 0 
              else 'Negative' if TextBlob(tweet.text).sentiment[0] < 0
              else 'Nuetral'] 
              for tweet in tweets]
# Note that we have again used list comprehension to build our array but with a conditional if/else statement for polarity

# We may now move this into a pandas dataframe
tweet_df = pd.DataFrame(data=user_data,
                    columns=['Created At', "User", 'Location', 'Text', 'Sentiment', 'Polarity'])

# Visual Analysis 1: Pie chart showing polarity across our sample

# Use Counter to count how many times each sentiment appears in our dataframe
polarity = tweet_df['Polarity']
counter_var = collections.Counter(polarity)

# Plot this as a simple pie chart utilisng matplot to show the distribution of sentiment across our tweets
fig = plt.pie(counter_var.values(), labels=counter_var.keys(), autopct='%1.0f%%',
              colors=['red', 'blue', 'green'])

plt.title("Polarity of Tweets Using #DominicCummings")
plt.show()
