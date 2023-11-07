#!/usr/bin/python3
"""API MODULE"""
import requests


def top_ten(subreddit):
    """ a function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit

    Args: https://www.reddit.com/r/python/top.json?limit=10

    """
    if subreddit is None or type(subreddit) is not str:
        print(None)

    headers = {'User-Agent': 'VUTHhzWkxrTG56djBsR3dhN'}
    parameters = {'limit': 10}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)
    if response.status_code == 404:
        print(None)
    data = response.json()
    if data is None:
        print(None)

    posts = data.get('data').get('children')

    [print(post.get('data').get('title')) for post in posts]
