#!/usr/bin/python3
"""API MODULE"""
import requests


def count_words(subreddit, word_list, words=None, after=None):
    """ a function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit

    Args: https://www.reddit.com/r/python/top.json?limit=10

    """
    if subreddit is None or type(subreddit) is not str:
        print(None)
    if words is None:
        words = {}
        for word in word_list:
            word_lower = word.lower()

            if word_lower in words:
                words[word_lower]['count'] += 1
            else:
                words[word_lower] = {'word': word_lower, 'count': 1, 'sum': 0}

    headers = {'User-Agent': 'VUTHhzWkxrTG56djBsR3dhN'}
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
    for post in posts:
        title = (post.get('data').get('title')).lower()
        for tile in title.split(' '):
            if tile in words.keys():
                words[tile]['sum'] += words[tile]['count']

    if after is None:
        for key, val in words.items():
            if val['sum'] != 0:
                print(f"{key}: {val['sum']}")
    else:
        print(after)
        count_words(subreddit, word_list, words, after)
