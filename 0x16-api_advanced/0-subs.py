#!/usr/bin/python3
"""
 function that queries the Reddit API and returns the number of subscribers
"""

import os
import requests


def number_of_subscribers(subreddit):
    '''
        returns the number of subscribers for a given subreddit
    '''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/58.0.3029.110 Safari/537.3')
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
