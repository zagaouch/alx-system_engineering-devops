#!/usr/bin/python3
"""
    Query reddit api top ten- posts titles for a subredit
"""

import requests
from os import sys

subredit = sys.argv[1]


def top_ten(subreddit):
    """
        Get top 10 hot posts titles for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get("title"))
    except Exception:
        print("None")
