#!/usr/bin/python3
"""script"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "andydev_"},
                            allow_redirects=False, params={"limit": 1000,
                            "after": after})
    if response.status_code == 200:
        pag_control = response.json().get("data").get("after")
        if pag_control is not None:
            recurse(subreddit, hot_list, pag_control)
        obj = response.json().get("data").get("children")
        for item in obj:
            hot_list.append(item.get("data").get("title"))
        return hot_list
    else:
        print("None")
