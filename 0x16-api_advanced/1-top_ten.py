#!/usr/bin/python3
"""Module for printing the top 10 titles of hot posts in a subreddit."""

import requests


def top_ten(subreddit):
    '''Prints the titles of the top 10 hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None

    Prints:
        The titles of the top 10 hot posts for the subreddit.
        Prints None if the subreddit is not found or an error occurs.
    '''
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    USERAGENT = {
        'User-Agent': 'Unix:com.alx.apiadvanced:task1 (by /u/_mundia_nderi_)'}
    req = requests.get(URL, headers=USERAGENT)

    if req.status_code != 200:
        print(None)
        return

    jreq = req.json()
    data_path = jreq['data']['children']

    for i in range(10):
        print(data_path[i]['data']['title'])
