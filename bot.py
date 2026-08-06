from google_sheet import next_tweet,mark_posted
from twitter_client import post
row,text=next_tweet()
if row:
    post(text)
    mark_posted(row)
    print("Posted:",text)
else:
    print("No tweets remaining")
