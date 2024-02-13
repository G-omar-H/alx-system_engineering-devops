#!/usr/bin/python3
"""
python script to fetch reddit API
"""

import requests

after = None
count = 0


def count_words(subreddit, word_list):
    """
    count the number of occurence of a given keyword
    from reddit api titles

    Args:
        subreddit (string): subreddit to fetch
        word_list (list): list of keyword to count for matche
    """
    global after
    global count
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
    }
    req = requests.get(url, params=params, headers=headers,
                       allow_redirects=False)
    if req.status_code == 200:
        res = req.json()
        titles = [c["data"]["title"] for c in res["data"]["children"]]
        for title in titles:
            print(title)