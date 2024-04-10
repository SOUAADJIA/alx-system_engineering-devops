#!/usr/bin/python3
"""Module docs"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to retrieve hot articles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My Reddit Client (by /u/your_username)"}

    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            hot_list.append(title)

    after = data.get("after")
    if after:
        recurse(subreddit, hot_list, after)

    return hot_list
