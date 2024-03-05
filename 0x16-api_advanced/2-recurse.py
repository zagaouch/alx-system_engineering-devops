#!/usr/bin/python3
"""Query reddit api top ten- posts titles for a subredit recursively"""

import requests
from os import sys

subredit = sys.argv[1]


def recurse(subreddit, hot_list=[], after=None):
    """Get top allhot posts titles for a given subreddit recursively"""
    if subreddit is None or not isinstance(subreddit, str):
        return None
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100,
              after: after}
    try:
        response = requests.get(url, headers=headers,
                                params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return None
        data = response.json().get('data')
        hot_list.extend([post.get('data').get('title')
                        for post in data.get('children')])
        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
