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

# Enter in a list of strings, each of which is the @username of a verified news provider account
search = api.user_timeline(screen_name = 'BBCWorld', count = 100, include_rts = False) 


WIP
