# Twitter_Diplomacy_Project
Analysis of use of Twitter Diplomacy by President Trump and Secretary Pompeo. Project conducted jointly for an Applied Statistical Methods course and International Relations Seminar.

## Files and Descriptions:
  
**'trump_tweets_code.py'**  
Code used to request user @realDonaldTrump's timeline from Twitter Developer API, and put raw twitter response into json. Developer keys removed for privacy.
  
**'pompeo_tweets_code.py'**  
Code used to request  user @SecPompeo's timeline from Twitter Developer API, and put raw twitter response into json. Developer keys removed for privacy.
  
**'tweet_processing_code.py'**  
Code used to pre-process the json files of tweets and put into pandas DataFrame/ export to csv. Processing steps include creation of hashtag text variable, creation of mention names variable, and removing links from tweet text. Subsetting steps include ensuring dataframes from each user only include tweets from same time range, excluding tweets that only include a link and no text, only including original tweets (no retweets of other users' statuses), and removing variables not relevant to this analysis.
  
 **'trump.csv'**  
CSV file of user @realDonaldTrump's tweets as requested and pre-processed in code files described above. File also includes 2 manually added columns/ variables: an 'is_diplomatic' binary variable and 'entities_mentioned' string variable. The 'is_diplomatic' variable takes a value of 1 if the tweet mentions/discusses a foreign entity (country name, leader, region, etc.) and can therefore be thought of as related to diplomacy, and 0 otherwise. The 'entities_mentioned' variable indicates which entities were mentioned in a given tweet, though simplified to prioritize country names (for example, tweets mentioning Macron or Paris are simplified to 'France').   
  
 **'pompeo.csv'**  
 CSV file of user @SecPompeo's tweets as requested and pre-processed in code files described above. File also includes 2 manually added columns/ variables: an 'is_diplomatic' binary variable and 'entities_mentioned' string variable. The 'is_diplomatic' and 'entities_mentioned' variables are coded as described in the 'trump.csv' description above.
  
**'analysis_code.ipynb'**  
Code used to perform statistical analysis of above data files of tweets. Includes: permutation test for the difference in proportions of diplomatic tweets between users, permutation test for the difference in number of unique entities referenced in tweets by each user, permutation test for the difference in relative frequency of specific diplomatic entity references in diplomatic tweets for each user.
  
**'graph_code.Rmd'**  
Code used to create graphs visualizing the data as related to the topic of this project. 
