# Twitter_Diplomacy_Project
Analysis of use of Twitter Diplomacy by President Trump and Secretary Pompeo. Project conducted jointly for an Applied Statistical Methods course and International Relations Seminar.

## Files and Descriptions:

**'Twitter Diplomacy Final Project.pdf'**
Project write-up. Description of data, explanation of data processing and analysis steps, graphical summaries of data, and analysis of study results. 
  
**'trump_tweets_code.py'**
Code used to request user @realDonaldTrump's timeline from Twitter Developer API, and put raw twitter response into json. Developer keys removed for privacy.
  
**'pompeo_tweets_code.py'**
Code used to request  user @SecPompeo's timeline from Twitter Developer API, and put raw twitter response into json. Developer keys removed for privacy.
  
**'tweet_processing_code.py'**
Code used to pre-process the json files of tweets and put into pandas DataFrame/ export to csv. Processing steps include creation of hashtag text variable, creation of mention names variable, and removing links from tweet text. Subsetting steps include ensuring dataframes from each user only include tweets from same time range, excluding tweets that only included a link and no text, only including original tweets (no retweets of other users' statuses), and removing variables not relevant to this analysis.
  
**'analysis_code.ipynb'**
Code used to perform statistical analysis of tweets as processed above (an after the manual addition of 'is_diplomatic binary variable and 'entities_mentioned' string variable. Includes: difference in proportions of diplomatic tweets between users and permutation test, difference in number of unique entities referenced in tweets between users and permutation test, difference in relative frequency of specific diplomatic entity references in diplomatic tweets for each user and permutation test.
  
**'graph_code.Rmd'**
Code used to create graphs visualizing the data as it relates to the topic of this project. 
