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

    url = 'https://www.reddit.com'
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'My Reddit Scraper'
    }
    response = requests.get(
        f'{url}/r/{subreddit}/.json?sort=top&limit=10',
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        for post in response.json().get('data', {}).get('children', [])[:10]:
            print(post['data']['title'])
    else:
        print("None")
