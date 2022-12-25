import time
import random
import tweepy
from datetime import datetime
from credentials import *
import quotes


old_id = None
# def checkForCorrectTime():
#     current_time = datetime.now().strftime("%H:%M:%S")
#     if current_time == "15:00:00" :
#         print("Do Action")
#         checkForCorrectTime()
#     else:
#         checkForCorrectTime()
#
# checkForCorrectTime()
def performQueryAndReply(old_id=None):

 auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
 api = tweepy.API(auth)
 query_string = "of 100DaysOfCode -filter:retweets"
 for tweet in tweepy.Cursor(api.search_tweets,query_string).items():
     try:

         # get tweet details
         print("Tweet is from @", tweet.user.screen_name)
         user_screen_name = tweet.user.screen_name
         user_id = tweet._json["id"]
         # tweet id must not repeat again
         if tweet.id != old_id:
             old_id = tweet.id
             print(tweet.text)

             # select a random quote
             my_reply = random.choice(quotes.quotes)

             # reply to tweet
             api.update_status(my_reply, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
             print("Replied to tweet=", my_reply)
             # time.sleep(86400)
             break
         else:
             continue

     except tweepy.errors.TweepyException as exception :
         print(exception)
         continue

     # performQueryAndReply()


performQueryAndReply()


# Check if script has run successfully
if performQueryAndReply():
    # Exit script if script has run successfully
    exit()


