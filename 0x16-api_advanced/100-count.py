#!/usr/bin/python3

"""
Recursive function to count occurrences of keywords in the titles of
hot articles in a subreddit.
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Counts occurrences of keywords in the titles of hot
    articles in a subreddit.
    """
    if count_dict is None:
        count_dict = {}

    if not word_list:
        return

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    word_lower = word.lower()
                    current_count = count_dict.get(word_lower, 0)
                    count_dict[word_lower] = current_count + 1
        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, after, count_dict)
        else:
            sorted_count = sorted(
                count_dict.items(),
                key=lambda x: (-x[1], x[0])
                )

            for word, count in sorted_count:
                print('{}: {}'.format(word, count))

    elif response.status_code == 404:
        print(None)
