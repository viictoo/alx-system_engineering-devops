#!/usr/bin/python3
"""API MODULE"""
import requests


def top_ten(subreddit):
    """ a function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit

    Args: https://www.reddit.com/r/python/top.json?limit=10

    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    headers = {
        'User-Agent': 'VUTHhzWkxrTG56djBsR3dhN',
    }
    parameters = {'limit': 10}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 404:
        return 0
    data = response.json()

    posts = data.get('data').get('children')

    [print(post.get('data').get('title')) for post in posts]