import praw

from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT


def connect_to_reddit():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )
    return reddit


def fetch_top_posts(subreddit_name):
    return connect_to_reddit().subreddit(subreddit_name).top(limit=None)


def fetch_hot_posts(subreddit_name):
    return connect_to_reddit().subreddit(subreddit_name).hot(limit=None)


def fetch_new_posts(subreddit_name):
    return connect_to_reddit().subreddit(subreddit_name).new(limit=None)


def fetch_controversial_posts(subreddit_name):
    return connect_to_reddit().subreddit(subreddit_name).controversial(limit=None)


def fetch_rising_posts(subreddit_name):
    return connect_to_reddit().subreddit(subreddit_name).rising()
