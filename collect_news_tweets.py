# Import libraries
import tweepy as tweepy
import pandas as pd
import re

# You should have worked through the collect_tweets.py file and have imported the necessary api keys and auth permissions

# We've searched for hashtags but what about specific users? We can use the same code but with the user_timeline() tweepy function instead
tweets = tweepy.Cursor(api.user_timeline,
              screen_name="BBCWorld",
              lang="en",
              include_rts = False,
              since="2020-06-01").items(50)

user_data = [[tweet.created_at, tweet.user.name, remove_characters(tweet.text)] for tweet in tweets]

# We may now move this into a pandas dataframe again
tweet_df = pd.DataFrame(data=user_data,
                    columns=['Created At', 'User', 'Text'])


# So what if we wanted a dataframe with the latest tweets from a range of news sources? We will utilise a for loop
users = ["cnn", "BBCWorld", "SkyNews", "telegraph", "rt_com", "guardiannews", "ajenglish", "financialtimes"] # Ensure your usernames are verified and correct
df = []
for i in users: # For each user -> perform the user_timeline scrape function
    tweets = tweepy.Cursor(api.user_timeline,
                  screen_name=i,
                  lang="en",
                  include_rts = False,
                  since="2020-06-01").items(10)

    user_data = [[tweet.created_at, tweet.user.name, remove_characters(tweet.text)] for tweet in tweets]
    tweet_df = pd.DataFrame(data=user_data,
                    columns=['Created At', 'User', 'Text'])
    df.append(tweet_df)
    
# The for loop creates a list of dataframes for each user, then we simply append them to each other using the concat() function
complete_table = pd.concat(df, ignore_index=True)

# You will be left with a dataframe showing the latest tweets from each news source, allowing you to perform further analysis such as sentiment or word count
