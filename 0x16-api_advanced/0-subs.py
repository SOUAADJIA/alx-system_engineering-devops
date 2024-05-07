#!/usr/bin/python3
"""How many subs?"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "My Reddit Scraper"})

    if response.status_code == 200:
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    else:
        return 0

