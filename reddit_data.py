import praw
import config
import re


# Reddit Functions
def bot_login():
    reddit = praw.Reddit(username=config.reddit_username,
                         password=config.reddit_password,
                         client_id=config.client_id,
                         client_secret=config.client_secret,
                         user_agent="Manga Disc Site V.1")
    return reddit


def get_from_reddit(item):
    results = {}
    reddit = bot_login()
    reddit_posts = reddit.subreddit('manga').search(
        'disc '+item,
        sort='new',
        time_filter='week')
    for item in reddit_posts:
        results[item.title] = {'rlink': item.permalink,
                               'mlink': item.url}
    return results
