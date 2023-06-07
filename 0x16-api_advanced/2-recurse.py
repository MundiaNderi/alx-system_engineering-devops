#!/usr/bin/python3
"""Module for retrieving a list of titles for hot articles
in a subreddit recursively."""

import requests


def recurse(subreddit, hot_list=[], count=0, after_val=None):
    '''Returns a list of titles for hot articles in a subreddit
    using recursive calls.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): A list to store the titles of hot
        articles. Default is an empty list.
        count (int, optional): The number of recursive calls made.
        Default is 0.
        after_val (str, optional): The value used for pagination.
        Default is None.

    Returns:
        list: A list of titles for hot articles in the subreddit.
            Returns None if the subreddit is not found or an error occurs.
    '''
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    USERAGENT = {
        'User-Agent': 'Unix:com.alx.apiadvanced:task3 (by /u/_mundia_nderi_)'}
    params = {'limit': 100}

    if count > 0:
        params['after'] = after_val

    req = requests.get(URL, headers=USERAGENT, params=params)

    if req.status_code != 200:
        return None

    jreq = req.json()
    data_path = jreq['data']['children']

    for i in range(len(data_path)):
        hot_list.append(data_path[i]['data']['title'])

    count += 1
    after_val = jreq['data']['after']

    if after_val is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, count, after_val)
