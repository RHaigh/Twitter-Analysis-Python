import tweepy
import re
import pandas as pd
import itertools
import collections
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# This file assumes you have created a list of tweets as detailed in the collect_tweets.py file within this repository

# We will utilise the same text cleaning custom function
def remove_characters(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

## Word Count Analysis
# Using the same structure as in collect_tweets.py, we collect tweets based on a chosen hashtag

tweets = tweepy.Cursor(api.search,
              q="#dominiccummings -filter:retweets",
              lang="en",
              since="2020-05-20").items(100)

# Specify we wish to look solely at the text subsection
tweets = [tweet.text for tweet in tweets]

# Remove unnecessary characters
tweets = [remove_characters(tweet) for tweet in tweets]

# Split words and remove upper case characters
tweet_words = [tweet.lower().split() for tweet in tweets]

# We must now remove stop words using the nltk library (stop words are ones such as 'the' or 'is')
nltk.download('stopwords')
# Note that if you have not downloaded the nltk word libraries before, you may hit an SSL error. A guide to solving this can be found at: https://github.com/gunthercox/ChatterBot/issues/930

stop_words = set(stopwords.words('english'))
tweets = [[word for word in tweet_words if not word in stop_words]
              for tweet_words in tweet_words]
              
# List of all non-stop words across our tweets using the itertools library
all_words = list(itertools.chain(*tweet_words))

# Create counter to iterate over this list
word_count = collections.Counter(all_words)

# We now have a list of the most commonly used words and their frequency
word_count.most_common(15)

# Put this list into a pandas dataframe as we did with our tweets in collect_tweets.py
tweet_df = pd.DataFrame(word_count.most_common(15),
                             columns=['words', 'count'])
                             
# Finally we can us matplotlib to plot a horizontal bar graph of tweet frequency as a visual aid
fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
tweet_df.sort_values(by='count').plot.barh(x='words',
                      y='count',
                      ax=ax,
                      color="purple")

ax.set_title("Most Common Words Found in Tweets")

plt.show()
