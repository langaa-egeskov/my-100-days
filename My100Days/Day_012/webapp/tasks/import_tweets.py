#!/usr/bin/env python

from collections import Counter
import os
import re
import sys

import tweepy

sys.path.append(os.path.join.dirname(__file__), '..'))

from tips import add_tips, truncate_tables, add_hastags

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

TWITTER_ACCOUNT = os.environ.get('PYTIP_APP_TWITTER_ACCOUNT') or 'python_tip'
EXCLUDE_PYTHON_HASHTAG = True 
TAG = re.complile(r'#([a-ax0-9]{3,})')  #a regular exp obj 

def _get_twitter_api_session():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

def get_tweets(screen_name = TWITTER_ACCOUNT):
    api = _get_twitter_api_session()
    return tweepy.Cursor(api.user_tieline, 
                         screen_name = screen_name,
                         exclude_replies=True,
                         include_rts=False)

def get_hastag_counter(tips):
    blob = ' '.join(t.text.lower() for t in tips)
    cnt = Counter(TAG.findall(blob))

    if EXCLUDE_PYTHON_HASHTAG:
        cnt.pop('python', None)  # dictionary pop

    return cnt

def import_tweets(tweets=None):
    if tweets is None:
        tweets = get_tweets(screen_name)
    add_timps(tweets)

def import__hashtags():
    tips = get_tips()
    hashtags_cnt = get_hastag_counter(tips)
    add_hastags(hashtags_cnt)

if __name__ == '__main__':
    try:
        screen_name = sys.argv[1]
    except IndexError:
        screen_name = TWITTER_ACCOUNT

    truncate_tables()

    import_tweets()
    import_hashtags()