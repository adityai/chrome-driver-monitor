import requests
import tweepy
import os
open('current.txt', 'a').close()

r = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE')
f = open("current.txt", "r")
previous = f.read()

if r.text != previous:
    print("Changed")
    f = open("current.txt", "w")
    f.write(r.text)
    print("Driver version changed from " + previous + " to " + r.text)
    # personal details 
    consumer_key=os.getenv('CONSUMER_KEY')
    consumer_secret=os.getenv('CONSUMER_SECRET')
    access_token=os.getenv('ACCESS_TOKEN')
    access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')

    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

    # authentication of access token and secret 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 

    # update the status 
    api.update_status(status ="Chrome Driver version changed from " + previous + " to " + r.text + " at https://chromedriver.chromium.org/")
