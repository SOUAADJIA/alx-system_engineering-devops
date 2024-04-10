#!/usr/bin/python3
"""How many subs?"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My Reddit Scraper"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json().get("data")
        if data:
            return data.get("subscribers", 0)
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
