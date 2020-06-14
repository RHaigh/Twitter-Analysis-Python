# Import libraries
import tweepy as tweepy
import pandas as pd
import re

# Enter in twitter api details here
consumer_key = '2LphmpVvZKjodaXA1LxuEwoXd'
consumer_secret = 'zrKVohL2RlOOfUKqspWdwSe3AUUx6aOaHDLoBx3C8EcPt1vwJV'
access_key= '1092147060936265729-kwwbyHp9PAfJkcsM7n6ZEai7wiYf2x'
access_secret = '4cPHmvp2nxI2BiayXzuECIgG7PJqb0ogQiNRrPqx7s8no'

# These credentials are passed to Tweepys open-standard authorization protocol letting it know that it is allowed to access your twitter developer account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# We've searched for hashtags but what about specific users? We can use the same code but with the user_timeline function instead
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
for i in users: # For each user > perform the user_timeline scrape function
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

