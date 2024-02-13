#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

after = None
count = 0


def recurse(subreddit, hot_list=[]):
    """
        return a list of  the titles of
        the 10 hottest posts on a given subreddit.
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
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    results = response.json().get("data")
    after = results.get("after")
    count = results.get("dist")
    [hot_list.append(c.get("data").get("title"))
        for c in results.get("children")]
    if after is not None:
        recurse(subreddit, hot_list)
    return hot_list
