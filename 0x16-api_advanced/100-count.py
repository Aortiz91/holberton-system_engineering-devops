#!/usr/bin/python3
"""
    recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords.
"""

from collections import Counter
import requests


def count_words(subreddit, word_list, hot_list=[], after="", word_dict={}):
    """
        recursive function that queries the Reddit API, parses the title of all
        hot articles, and prints a sorted count of given keywords.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "andydev_"},
                            allow_redirects=False, params={"after": after,
                            "limit": 100})
    if response.status_code == 200:
        pag_control = response.json().get("data").get("after")
        if pag_control is not None:
            return count_words(subreddit, word_list, hot_list, pag_control, word_dict)
        obj = response.json().get("data").get("children")
        for item in obj:
            hot_list.append(item.get("data").get("title"))
        str = ""
        for titles in hot_list:
            str = str + titles + " "
        for word in word_list:
            for item in (str.split(" ")):
                
                print(word)
#            if item.lower() === word_list:
#               word_dict["item"] = item
#        print(word_dict)
    #final = Counter(word_dict.values())
    #print((final))
