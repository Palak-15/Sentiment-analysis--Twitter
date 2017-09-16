import tweepy
import csv
import os
from textblob import TextBlob
#from twiiter api , keys and access
consumer_key='*****************************'
consumer_secret='**************************************'
Access_token='********************************************'
Access_secret='*****************************************'

#Authentication to your Twitter account
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(Access_token,Access_secret)

api=tweepy.API(auth)

#now we are done with authentication, we can search , create and delete tweets

public_tweets=api.search('Trump')

writer = csv.writer(open("N:/Programs/Senti", 'w'))


for tweet in public_tweets:
	#print(tweet.text)   #here we are print the text of tweet which has string trump in it
	
	analysis=TextBlob(tweet.text)
	 #sentiment has 2 , polarity for how +ve or-ve the tweet is and subjectivity is how  much opinion is v/s factual
	if(analysis.sentiment.polarity >0 ):
		decis='Positive'
	else :
		decis='Negative'
	writer.writerow((tweet.text,decis))
	writer.writerow(os.linesep)
	
