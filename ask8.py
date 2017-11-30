#---------------ASKHSH 8-----------

import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = ""
consumer_secret =""
access_token = ""
access_secret = ""
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
print "I'm using python to mine twitter!"


screenname1=raw_input("Dwse 1o onoma xrhsth tweeter xwris '@' \n ")
screenname2=raw_input("Dwse 2o onoma xrhsth tweeter xwris '@' \n ")
k=0
public_tweets = api.user_timeline(screen_name=screenname1,count=10)
for tweet in public_tweets :
    k=k+len(tweet.text.split())
v=0
public_tweets = api.user_timeline(screen_name=screenname2,count=10)
for tweet in public_tweets :
    v=v+len(tweet.text.split())

if (k>v):
    print("Perissoteres Lexeis exei o xrhsths  " + screenname1)
elif (k<v):
    print("Perissoteres Lexeis exei o xrhsths  " + screenname2)
else :
    print("kanenas den exei perisoteres lexeis")
