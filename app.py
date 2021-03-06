import tweepy
import os
import requests
import time
from dotenv import load_dotenv
import logging

load_dotenv()
# tls 1.2 error 
# https://stackoverflow.com/questions/53497/how-do-i-set-tls-1-0-as-default-in-python-requests


    
logging.basicConfig(filename='error.log', level=logging.INFO, format='%(asctime)s %(message)s')

# make get request from "https://programming-quotes-api.herokuapp.com/Quotes/random"
res = requests.get(
    "https://programming-quotes-api.herokuapp.com/quotes/random")


# get environment variables
bearer_token = os.environ.get("BEARER_TOKEN")

# make auth
auth = tweepy.OAuthHandler(consumer_key=os.environ.get("API_KEY"),consumer_secret=os.environ.get("API_KEY_SECRET"))
auth.set_access_token(os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth, wait_on_rate_limit=True)

logging.info("Authenticated")
if res.status_code == 200:
    logging.info("Request successful")
    # get the quote
    quote = res.json()
    
    api.update_status(status=f"""{quote['en']}\n- {quote['author']} \n\n#programming #quotes #quoteoftheday""")
    # make log
    time.sleep(3)
    logging.info("Tweet successful")
    logging.info(f"""{quote['en']}\n- {quote['author']} \n\n#programming #quotes #quoteoftheday""")
        # exit the program
    

else:
    logging.error("Request failed")
    
    logging.info(f"""{res.status_code} {res.text}""")
        # exit the program

exit(0)