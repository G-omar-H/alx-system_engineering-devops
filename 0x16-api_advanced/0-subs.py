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
import json
from sys import argv


def number_of_subscribers(subreddit):
    """
    get the numver of subscribers for a subreddit
    Args:
        subreddit (str): given subreddit from command line
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        req = requests.get(url, headers={"User-agent": "yourbot"},
                           allow_redirects=False)
        res = req.json()
    except Exception:
        return 0
    return res['data']['subscribers']
