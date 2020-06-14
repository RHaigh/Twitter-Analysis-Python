# Import libraries
import tweepy as tweepy
import pandas as pd
import re

# Enter in twitter api details here
consumer_key = 'key_string'
consumer_secret = 'key_string'
access_key= 'key_string'
access_secret = 'key_string'

# These credentials are passed to Tweepys open-standard authorization protocol letting it know that it is allowed to access your twitter developer account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Now you're ready to look for tweets. Define your hashtag and dates range and collect tweets using Cursor
tweets = tweepy.Cursor(api.search,
              q="#dominiccummings -filter:retweets",
              lang="en",
              since="2020-05-20").items(50)
# Control your no of collected tweets with .items()

# Cursor creates a cursor class object we may iterate over and print tweets
for tweet in tweets:
    print(tweet)

# Lets look at the output format of each of these tweets and what is contained in the json:
## Status(_api=<tweepy.api.API object at 0x1063d69d0>,
# _json={'created_at': 'Mon May 25 12:43:22 +0000 2020',
# 'id': 1264899863071858694,
# 'id_str': '1264899863071858694',
# 'text': '#DominicCummings announces he will do the #queensspeech this #Christmas .',
# 'truncated': False,
# 'entities':
#   {'hashtags': [{'text': 'DominicCummings', 'indices': [0, 16]},
#   {'text': 'queensspeech', 'indices': [42, 55]},
#   {'text': 'Christmas', 'indices': [61, 71]}],
#   'symbols': [],
#   'user_mentions': [],
#   'urls': []},
#   'metadata': {'iso_language_code': 'en', 'result_type': 'recent'},
#   'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
#   'in_reply_to_status_id': None,
#   'in_reply_to_status_id_str': None,
#   'in_reply_to_user_id': None,
#   'in_reply_to_user_id_str': None,
#   'in_reply_to_screen_name': None,
#   'user': {'id': 2659600959,
#     'id_str': '2659600959',
#     'name': 'Michael Dee',
#     'screen_name': 'MyScotlandpage',
#     'location': 'Glasgow, Scotland',
#     'description': "please don't add me to lists . This will result in an instant blocking #livingwithcancer not a #mcbot .",
#     'url': None,
#     'entities':
#       {'description': {'urls': []}},
#   'protected': False,
#   'followers_count': 1345,
#   'friends_count': 1352,
#   'listed_count': 23,
#   'created_at': 'Tue Jul 01 10:37:07 +0000 2014',
#   'favourites_count': 13061,
#   'utc_offset': None,
#   'time_zone': None,
#   'geo_enabled': False,
#   'verified': False,
#   'statuses_count': 65164,
#   'lang': None,
#   'contributors_enabled': False,
#   'is_translator': False,
#   'is_translation_enabled': False,
#   'profile_background_color': 'C0DEED',
#   'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png',
#   'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png',
#   'profile_background_tile': False,
#   'profile_image_url': 'http://pbs.twimg.com/profile_images/1259119759989313539/sTzJPGXS_normal.jpg',
#   'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1259119759989313539/sTzJPGXS_normal.jpg',
#   'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2659600959/1588366973',
#   'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED',
#   'profile_sidebar_fill_color': 'DDEEF6',
#   'profile_text_color': '333333',
#   'profile_use_background_image': True,
#   'has_extended_profile': False,
#   'default_profile': True,
#   'default_profile_image': False,
#   'following': False,
#   'follow_request_sent': False,
#   'notifications': False,
#   'translator_type': 'none'},
#   'geo': None, 'coordinates': None,
#   'place': None, 'contributors': None,
#   'is_quote_status': False,
#   'retweet_count': 0,
#   'favorite_count': 0,
#   'favorited': False,
#   'retweeted': False,
#   'lang': 'en'},

# Quite a lot of information, much of it unnecessary for our analysis. 

# First off, we will create a custom function to clean the text and remove additional characters and emojis using re (similar to gsub in R and tidyverse)
def remove_characters(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

# We will then filter results by our chosen fields with list comprehension whilst cleaning up the results using our remove_characters function
user_data = [[tweet.created_at, remove_characters(tweet.user.name), tweet.user.location, remove_characters(tweet.text)] for tweet in tweets]

# We can now move this into a pandas dataframe
tweet_df = pd.DataFrame(data=user_data,
                    columns=['Created At', "User", 'Location', 'Text'])
                    
tweet_df
