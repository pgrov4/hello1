print("Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).")

# created an API  with name priyankagro48 on twitter and also generated an access token for tht
print("Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.")
#google.com 216.58.221.36
# www.facebook.com 157.240.13.38
print("Q.3- Using Tweepy library try to extract tweets from Twitter.")
import tweepy
import textblob
from textblob import TextBlob
from tweepy.auth import OAuthHandler



consumer_key='bSmkwkT3vhyd88lURb10ZCiZq'
consumer_secret='CApGl8OhstDSoVHR1PvNeN93U4WjtshPYNP9PbGqG7o2XemBIx'
access_token='1006737019987472390-lWhAUDtEwd45lxaBuGE9gFKtkeXm02'
access_token_secret='PAJ2bDw3vCSAXKEkBQsHFEaJZqyyLBxNJJc158rli59mU'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)
public_tweets=api.search("#KKRvsCSK")
print(public_tweets)
#Oauth=tweepy.oAuthHandler(consumer_key,consumer_secret)
#b=tweepy.oauthHandler(1,2)

print("Q.4- What is a difference between library and API . Figure it out with examples.")

import requests#library
import json

# Make it a bit prettier..
print("-" * 30)
print("Trying to access youtube API This will show the Most Popular Videos on YouTube")
print("-" * 30)

# Get the feed
r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")# trying to access Youtube API
r.text

# Convert it to a Python dictionary
data: object = json.loads(r.text)

# Loop through the result.
# for item in json.loads(r.text):
#         #data["d"]["item"]:
#
#     print("Video Title: ", (item["title"]))
#
#     print("Video Category:",(item['category']))
#
#     print("Video ID:" (item['id']))
#
#     print("Video Rating: ", (item['rating']))
#
#     print("Embed URL: ", (item['player']['default']))
#
#     print("")

print("Q.5- Try to access Spotify API . Find out some library for it and play some music.")
from pygame import mixer
mixer.init()
mixer.music.load("C:\\Users\\agrover\\Desktop\\whatsappData\\net.whatsapp.WhatsApp\\Library\\Media\\919796281149-1423935497@g.us\\4\\6.mp3")
mixer.music.play()
