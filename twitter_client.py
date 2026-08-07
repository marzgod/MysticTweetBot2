import os
import tweepy

client = tweepy.Client(
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
    wait_on_rate_limit=True,
)

def verify_auth():
    me = client.get_me(user_auth=True)
    print("Authenticated as:", me.data)

def post_tweet(text):
    verify_auth()
    response = client.create_tweet(text=text, user_auth=True)
    print(response)
