import time
import random
import tweepy
import requests
import json
from datetime import datetime
from io import BytesIO
from PIL import Image
from credentials import *
import quotes

import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=gen_ai_api_key)


text_model = genai.GenerativeModel('gemini-pro')
vision_model = genai.GenerativeModel('gemini-1.5-flash')

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

client = tweepy.Client(bearer_token,consumer_key,consumer_secret,access_token,access_token_secret)
auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret,access_token,access_token_secret)
api = tweepy.API(auth)



def postMeme():
  try:
    rand_num = random.randint(50 , 1500 )
    urlstring = "https://tg.i-c-a.su/media/programmerjokes/" + str(rand_num)
    json_response = requests.get(urlstring)
    meme_img_pil = Image.open(BytesIO(json_response.content))
    prompt = "Write a half liner caption suitable for this image to be shown as a meme to GenZ audience.Add suitable emoji in the text where ever required.Just write the caption right away.Please dont start like this: Here the half line ......"
    response = vision_model.generate_content([prompt,meme_img_pil], stream=True)
    response.resolve()


    # Save image in memory
    meme_img_bytes = BytesIO()
    meme_img_pil.save(meme_img_bytes, format='JPEG')
    meme_img_bytes.seek(0)

    media = api.media_upload(filename="meme of the day",file=meme_img_bytes)
    sequenceString = "\n.\n.\n.\n.\n.\n.\n."
    text = response.text + sequenceString + "\n#programminghumor #technology #100DaysOfCode"
    client.create_tweet(text=text,media_ids=[media.media_id_string])

  except Exception as e:
      print(e)


def postTechPrepContent():
    prompt = ""
    with open("techContentPrompt.txt","r") as file:
        prompt = file.read()

    response = text_model.generate_content(prompt)
    client.create_tweet(text=response.text)

def performQueryAndReply(old_id=None):

 # make GET request for joke
 json_response = requests.get("https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit")
 json_object_text = json_response.text
 joke_dict = json.loads(json_object_text)
 joke_org_text = ""
 if joke_dict["type"] == "single":
     joke_org_text = joke_dict["joke"]
 else:
     joke_org_text = joke_dict["setup"] + "\n\n" + joke_dict["delivery"]

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

             # tweet the joke
             api.update_status(joke_org_text)

             time.sleep(15)

             # reply to tweet
             api.update_status(my_reply, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
             print("Replied to tweet=", my_reply)
             exit()
         else:
             continue

     except tweepy.errors.TweepyException as exception :
         print(exception)
         continue

# performQueryAndReply()
postMeme()
postTechPrepContent()

#performQueryAndReply()

# # Check if script has run successfully
# if performQueryAndReply():
#     # Exit script if script has run successfully
#     exit()


