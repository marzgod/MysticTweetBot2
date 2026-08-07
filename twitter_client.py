import os

import tweepy


def post_tweet(text: str) -> None:
    if not text:
        raise ValueError("Tweet text is empty.")

    client = tweepy.Client(
        consumer_key=os.environ["API_KEY"],
        consumer_secret=os.environ["API_SECRET"],
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
    )

    response = client.create_tweet(text=text)

    if not response.data:
        raise RuntimeError("X did not return tweet data.")
