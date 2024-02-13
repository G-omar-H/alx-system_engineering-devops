#!/usr/bin/python3
"""
python script to fetch a given subreddit
from commandline api and
return number of subscribers
return:
    number of subscribers to the subreddit
    0 if wrong subreddit
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    get the numver of subscribers for a subreddit
    Args:
        subreddit (str): given subreddit from command line
    """
    try:
        url = f"https://www.reddit.com/subreddits/search.json?q={subreddit}"
        req = requests.get(url, headers={"User-agent": "yourbot"})
    except Exception:
        return 0
    req = req.json()
    total = 0
    for r in req["data"]["children"]:
        total += r["data"]["subscribers"]
    return total
