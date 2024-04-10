#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints titles of the first 10 hot posts for a given subreddit.

    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        if data:
            for post in data:
                print(post["data"]["title"])
        else:
            print("No posts found in the subreddit:", subreddit)
    else:
        print("None")
