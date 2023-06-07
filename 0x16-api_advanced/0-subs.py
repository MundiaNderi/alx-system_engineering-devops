#!/usr/bin/python3
"""Module for retrieving the total number of subscribers to a subreddit."""

import requests


def number_of_subscribers(subreddit):
    '''Function that returns the total number of subscribers to a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The total number of subscribers to the subreddit.
            Returns 0 if the subreddit is not found or an error occurs.
    '''
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    USERAGENT = {
        'User-Agent': 'Unix:com.alx.apiadvanced:task0 (by /u/_mundia_nderi_)'}
    req = requests.get(URL, headers=USERAGENT)

    if req.status_code != 200:
        return 0

    jreq = req.json()
    return jreq['data']['subscribers']
