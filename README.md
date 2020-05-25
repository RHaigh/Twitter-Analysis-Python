# Twitter Analysis with Python
An example of code demonstrating how to interact with the Twitter API to collect tweets with specific hashtags and then analyse this data for sentiment and location using the Python programming language

Author - Richard Haigh

Date of initial upload - 25/05/2020

Written - Python3.8

Environment - PyCharm Community 2020.1.1

Libraries: tweepy v3.5.0

An example of code demonstrating how to interact with the Twitter API to collect tweets with designated hashtags and then analyse this data for sentiment and location.

In order to utilise this code, you will require:

A twitter developer account
A google developer account with an activated GeoCoding API key
A helpful guide on how to achieve this (with visuals) can be found here: https://www.extly.com/docs/autotweetng_joocial/tutorials/how-to-auto-post-from-joomla-to-twitter/apply-for-a-twitter-developer-account/#apply-for-a-developer-account

The code comments will show where to insert your keys in string format. Note that depending on the power of your system, collecting tweets may take several minutes. Tweets collected are limited to 18000 every 15 minutes by the API.

The individual elements: API interaction, location and sentiment analysis, have been separated into individual files for ease of understanding. You may collect tweets of a particular hashtag, or from specific accounts then you can simply run subsequent graphical components for more in-depth analysis.
