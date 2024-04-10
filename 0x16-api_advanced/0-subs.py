#!/usr/bin/python3
"""How many subs?"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    url = 'https://www.reddit.com'
    header = {
        'Accept': 'application/json',
        'User-Agent': 'My Reddit Scraper'
    }
    response = requests.get('{}/r/{}/about/.json'.format(url, subreddit),
                            headers=header,
                            allow_redirects=False
                            )
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
