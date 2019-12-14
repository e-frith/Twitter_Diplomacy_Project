#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:24:58 2019

Applied Statistical Methods Final Project
Code Used to Download @SecPompeo Twitter Timeline

@author: Ellie Frith
"""

from urllib.parse import quote
import requests
import base64
import json

# From Twitter dev app:
key = '' # removed for privacy
secret_key = '' # removed for privacy


# URL encode consumer API key and secret API key according to RFC 1738
url_key =  quote(key)
url_secret = quote(secret_key)

my_string = url_key+':'+ url_secret
bearer_b64 = base64.b64encode(bytes(my_string, 'utf-8')).decode('utf-8')


# Request access token:
auth_headers = {
        'Authorization': 'Basic ' + bearer_b64,
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        }

auth_response = requests.post(
        url = 'https://api.twitter.com/oauth2/token',
        headers = auth_headers,
        data = {'grant_type': 'client_credentials'})

access_token = auth_response.json()['access_token']

headers = {'Authorization': 'Bearer ' + access_token}



# Get 17 sets of 200 tweets from @SecPompeo (max = 3200)

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
REPEATS = 17
OUTPUT_FILE = './sec_pompeo_tweets.json'


request_params = { 
    'screen_name': 'SecPompeo',
    'max_id': 1196531848177950730, # max id of tweet on nov. 18
    'count': 200,
    'include_rts': 1,
    'tweet_mode': 'extended' 
    }

tweets = []

for i in range(REPEATS):
    
    # For the first iteration of this loop, use the given max_id
    if i == 0:
        twitter_response = requests.get(url=TWITTER_URL,
                                        params=request_params,
                                        headers=headers)
        
        if twitter_response.status_code != 200: 
            print('non-200 response for repeat, skipping')
            continue
        
        else:
            twitter_search_json = twitter_response.text
            tweet_list = json.loads(twitter_search_json)
            for i in tweet_list:
                tweets.append(i)
    
    # For all subsequent iterations of this loop, update the max_id
    # parameter with the last id of tweet_list - 1
    
    else:
        last_id = tweet_list[len(tweet_list)-1]['id']
        request_params.update({'max_id': last_id-1})
        
        twitter_response = requests.get(url=TWITTER_URL,
                                        params=request_params,
                                        headers=headers)
        
        if twitter_response.status_code != 200: 
            print('non-200 response for repeat, skipping')
            continue
        
        else:
            twitter_search_json = twitter_response.text
            tweet_list = json.loads(twitter_search_json)
            
            if len(tweet_list)>0:
                for i in tweet_list:
                    tweets.append(i)


        
json.dump(tweets, open(OUTPUT_FILE, 'w')) 