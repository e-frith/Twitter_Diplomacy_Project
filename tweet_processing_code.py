#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:09:26 2019

Applied Statistical Methods Final Project
Data Processing/ Formatting Code 

@author: Ellie Frith
"""


import pandas as pd
import numpy as np
import re

pompeo_df = pd.read_json('sec_pompeo_tweets.json')
trump_df = pd.read_json('trump_tweets.json')


#Response from Twitter API has lots of extraneous information and dense 
#dictionaries: want to extract the information useful for this analysis 
  

def media_type(extended_entities):
    
    '''This function extracts the media type of any media attached to
    a tweet (image, video, etc). If tweet has no media, the function
    will return a value of nan. '''
    
    if pd.isnull(extended_entities)==True:
        media = np.nan
    else:
        media = extended_entities['media'][0]['type']
    return(media)



def hashtag_text(entities):
    
    '''This function extracts hashtags from the dense 'entities' dictionary
    returned by Twitter's API. If tweet uses no hashtags, this function will
    return a value of nan.'''
    
    hashtags = entities['hashtags'] # user mentions is a list, which is empty if none
    hashtag_text = []
    
    if len(hashtags)==0:
        hashtag_text = np.nan
    else:
        for i in range(0, len(hashtags)):
            hashtag_text.append(hashtags[i]['text'])
            
    return(hashtag_text)
    
    

def mention_names(entities):
    
    '''This function extracts the names of any users mentioned from the dense
    'entities' dictionary returned by the twitter API. If the tweet does not 
    mention any users, this function will return a value of nan.'''
    
    mentions = entities['user_mentions'] # user mentions is a list, which is empty if none
    mention_names = []
    
    if len(mentions)==0:
        mention_names = np.nan
    else:
        for i in range(0, len(mentions)):
            mention_names.append(mentions[i]['name'])
            
    return(mention_names)

def remove_links(full_text):
    '''This function removes links in tweets, and replaces them with
    whitespace.'''
    sans_link = re.sub(r"http\S+",'',full_text)
    return(sans_link)
    
def tweet_length(clean_text):
    '''This function return the length (number of characters)
    in a cleaned tweet (without links)'''
    length = len(clean_text)
    return(length)


# Create column that indicates whether a tweet is original content by the user 
# (as opposed to retweet):
pompeo_df['original_tweet'] = pompeo_df.retweeted_status.isnull()
trump_df['original_tweet'] = trump_df.retweeted_status.isnull()

# Create column of tweet media types:
pompeo_df['tweet_media'] = pompeo_df.extended_entities.apply(media_type)
trump_df['tweet_media'] = trump_df.extended_entities.apply(media_type)

# Create column of hashtag text:
pompeo_df['hashtag_text'] = pompeo_df.entities.apply(hashtag_text)
trump_df['hashtag_text'] = trump_df.entities.apply(hashtag_text)

# Create column of mention names:
pompeo_df['mention_names'] = pompeo_df.entities.apply(mention_names)
trump_df['mention_names'] = trump_df.entities.apply(mention_names)

# Create column of cleaned full_text (without links)
pompeo_df['clean_text'] = pompeo_df.full_text.apply(remove_links)
trump_df['clean_text'] = trump_df.full_text.apply(remove_links)

# Create column of clean_text length (for later subsetting)
pompeo_df['tweet_length'] = pompeo_df.clean_text.apply(tweet_length)
trump_df['tweet_length'] = trump_df.clean_text.apply(tweet_length)



# Subset to ensure that we analyze/compare only original tweets by users, 
    # tweets that were not just a link (i.e. now with links replaced, 
    #tweets with length less than 5 characters), and tweets with
    # a comparable date range (i.e. excluding tweets with id's lower than the 
    # oldest tweet by Trump that Twitter would let me pull)
min_id = trump_df.id[len(trump_df)-1]

cond_1 = (pompeo_df['original_tweet']==True)
cond_2 = (pompeo_df['id']>=min_id)
cond_3 = (pompeo_df['tweet_length']>5)
pompeo_df = pompeo_df[cond_1&cond_2&cond_3]

cond_1 = (trump_df['original_tweet']==True)
cond_2 = (trump_df['tweet_length']>5)
trump_df = trump_df[cond_1&cond_2]




# Use only important columns, and create csv:

# Create column getting user info (to test whether all are from extracted user)
cols_list = ['created_at','id','clean_text','favorite_count','retweet_count',
             'original_tweet','tweet_media','hashtag_text','mention_names', 
             'in_reply_to_screen_name','in_reply_to_status_id','is_quote_status']

pompeo_df = pompeo_df[cols_list]
trump_df = trump_df[cols_list]
 
pompeo_df.to_csv('./pompeo.csv', index=False)
trump_df.to_csv('./trump.csv', index=False) 