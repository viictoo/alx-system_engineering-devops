#!/usr/bin/python3
"""API MODULE"""
import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0

    Args:
        subreddit (str): name of subreddit

    Returns:
        int: subscriber count for the subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    headers = {
        'User-Agent': 'VUTHhzWkxrTG56djBsR3dhN',
    }

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            return 0
        data = response.json()
        # print(dat
        # if data.status >= 400:
        #     return 0

        subs = data.get('data').get('subscribers')

        return subs if subs is not None else 0

    except requests.exceptions.RequestException as e:
        print(e)
        return 0
