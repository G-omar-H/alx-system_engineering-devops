#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?t=all".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 302:
        return None
    results = response.json().get("data")
    after = results.get("after")
    count = results.get("dist")
    [hot_list.append(c.get("data").get("title"))
        for c in results.get("children")]
    if after is not None:
        recurse(subreddit, hot_list, after, count)
    return hot_list
