#!/usr/bin/python3
"""API MODULE"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ a function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit

    Args: https://www.reddit.com/r/python/top.json?limit=10

    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    headers = {
        'User-Agent': 'VUTHhzWkxrTG56djBsR3dhN',
    }
    parameters = {'after': after}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)
    # print(response.json())
    if response.status_code >= 400:
        return None
    data = response.json()

    posts = data.get('data').get('children')
    after = data.get('data').get('after')

    [hot_list.append(post.get('data').get('title')) for post in posts]
    if len(hot_list) == 0 or posts is None:
        return None
    return hot_list if after is None else recurse(subreddit, hot_list, after)
